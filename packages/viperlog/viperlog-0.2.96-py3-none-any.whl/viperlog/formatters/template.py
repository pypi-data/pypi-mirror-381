import os
import re
from logging import LogRecord
from typing import Dict, Callable, Tuple, List, Optional, Protocol

#ModifierFn = Callable[[str], str] | Callable[[str,str], str]
ModifierFn = Callable[[str,str,str|None], str]
PlaceholderModifierDef = Tuple[ModifierFn|None,str,str|None]
from ..logger import getLogger

from datetime import datetime, UTC
from dataclasses import dataclass
from functools import lru_cache
#pattern = re.compile(r"\$\{([^}]+)\}")
pattern = re.compile(r"\$\{([^}]+)}")

DEFAULT_TEMPLATE:str = "${date} ${time} [${levelname_short|upper|pad_left=5|max_length=5}] ${message}"
PARSE_VARIABLES_IN_LOGMESSAGE:bool = os.getenv("PARSE_VARIABLES_IN_LOGMESSAGE", "true").lower() in ("true", "1", "yes", "y")


@dataclass(slots=True)
class TemplateColumn:
    type: str  # "literal" or "placeholder"
    #text: Optional[str] = None
    #variable: Optional[str] = None
    contents: Optional[str] = None
    modifiers: Optional[List[tuple]] = None

@lru_cache(maxsize=250)
def create_template_from_message(message:str)->"MessageTemplate|str":
    if not message or '${' not in message:
        return message
    return MessageTemplate(message)


class IMessageTemplate(Protocol):
    def render(self, record: LogRecord) -> str:...

class MessageTemplate:
    """
    Parses a message template for use in a formatter
    The style is:
    ${variable}
    ${variable|modifier1}
    ${variable|modifier1|modifier2}
    ${variable|modifier1|modifier2=mod2value}
    ${variable|modifier1|default=default value here}
    Modifiers are executed in order from left to right, so if you do a padding and a max_length then the order matters
    These will get replaced, what is left is passed to the standard python logging library

    You could use:
    ${asctime|leftpad=5} to print the time padded to 5 chars on the left.
    Options:
    - asctime
    - name
    -
    """
    _started_at:datetime = datetime.now(UTC)
    _modifier_lookup:Dict[str,ModifierFn] = {
        # modifier names should all be lowercase here
        "default": (lambda varname, x, dv : x if x and x != varname else dv),
        "upper": (lambda varname,x,_ : x.upper()),
        "lower": (lambda varname,x,_ : x.lower()),
        "trim": (lambda varname,x,_ : x.strip()),
        "max_length": (lambda varname,x,l : x[0:int(l)]),
        "pad_left": (lambda varname,x,l : str(x).ljust(int(l), ' ')),
        "pad_right": (lambda varname,x,l : str(x).rjust(int(l), ' ')),
        "pad_center": (lambda varname,x,l : str(x).center(int(l), ' ')),
    }

    def __init__(self, template:str = DEFAULT_TEMPLATE):
        self.template = template
        self._columns:List[TemplateColumn] = []
        self._parse_template()

    def _render_text(self, text:str, record:LogRecord) -> str:
       return text

    def _render_variable(self, variable: str, value: str, record:LogRecord) -> str:
        """Called after applying modifiers to the value"""
        return value

    def _prepare_variable(self, variable:str, value:str, record:LogRecord)->str:
        """ Called before applying modifiers to the value """
        return value

    def _get_variable_value(self, variable, record:LogRecord)->str:
        # process build-in variable names
        # TODO: complete this list
        if variable == 'message':
            # support variables in the message itself
            message = record.getMessage()
            if PARSE_VARIABLES_IN_LOGMESSAGE:
                message = create_template_from_message(message)
                if isinstance(message, MessageTemplate):
                    return message.render(record)
            return message
        elif variable == 'message_raw':
            # returns the message without any further processing
            return record.getMessage()
        elif variable == 'asctime':
            return "{:.3f}".format(record.relativeCreated)
            #diff = datetime.now(UTC) - MessageTemplate._started_at
            #return "{:.3f}".format(diff.total_seconds())
        elif variable == 'datetime':
            return datetime.now(UTC).isoformat().replace("+00:00", "Z")
        elif variable == 'date':
            return datetime.now(UTC).date().isoformat()
        elif variable == 'time':
            return datetime.now(UTC).time().replace(microsecond=0).isoformat()
        elif variable == 'name_short':
            # gets the last part of the name
            return record.name.split('.')[-1]
        elif variable == 'level':
            return record.levelname
        elif variable == 'levelname_short':
            if(record.levelno == 50):
                return "FATAL"
            elif(record.levelno == 40):
                return "ERROR"
            elif(record.levelno == 30):
                return "WARN"
            elif(record.levelno == 20):
                return "INFO"
            elif(record.levelno == 10):
                return "DEBUG"
            return record.levelname

        # attempt to fetch from record
        value = getattr(record, variable) if hasattr(record, variable) else None
        if value is not None:
            return str(value)

        # Fall back on variable name
        return str(variable)  # raw variable as fallback

    def _get_modifier_fn(self, modifier:str)->Optional[ModifierFn]:
        name = modifier.lower()
        if name in MessageTemplate._modifier_lookup:
            fn = MessageTemplate._modifier_lookup[name]
            return fn
        return None


    def render(self, record:LogRecord)->str:
        result = []
        for c in self._columns:
            if c.type == 'literal':
                #result.append(c['text'])
                result.append(self._render_text(c.contents, record))
            elif c.type == 'placeholder':
                variable = c.contents
                modifiers = c.modifiers
                #value:str = str(variable) # raw variable as fallback

                value = self._get_variable_value(variable, record)

                value = self._prepare_variable(variable, value, record)
                if modifiers:
                    modifier:PlaceholderModifierDef|None = None
                    for modifier in modifiers:
                        if not modifier[0]:
                            # missing function
                            continue
                        value = modifier[0](variable, value, modifier[2])
                result.append(self._render_variable(variable, value, record))
                #result.append(value)
            else:
                # this should never happen
                getLogger(self.__class__.__name__).error('Unknown column type ' + c['type'])

        return ''.join(result)

    def _parse_template(self):
        logger = getLogger(self.__class__.__name__)
        s = self.template
        results:List[TemplateColumn] = []
        last_end = 0

        for m in pattern.finditer(s):
            # literal before the match
            if m.start() > last_end:
                #results.append({"type": "literal", "text": s[last_end:m.start()]})
                results.append(TemplateColumn(type="literal", contents=s[last_end:m.start()]))

            # placeholder match
            parts = m.group(1).split("|")
            var = parts[0]
            mods = []
            for p in parts[1:]:
                name:str = p
                val:str|None = None
                fn:ModifierFn|None = None
                if "=" in p:
                    name, val = p.split("=", 1)
                #else:
                #    mods.append((p, None))
                fn = self._get_modifier_fn(name)
                if not fn:
                    logger.warning(f"Unknown modifier {name}")
                mods.append((fn, name, val))
            results.append(TemplateColumn(
                type="placeholder",
                contents=var,
                modifiers=mods
            ))
            #results.append({
            #    "type": "placeholder",
            #    "variable": var,
            #    "modifiers": mods
            #})

            last_end = m.end()

        # trailing literal
        if last_end < len(s):
            results.append(TemplateColumn(type="literal", contents= s[last_end:]))
            #results.append({"type": "literal", "text": s[last_end:]})

        self._columns = results

