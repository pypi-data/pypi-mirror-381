
import json
from logging import LogRecord
from typing import Optional

from .base import BaseFormatter
from .dict_formatter import DictFormatter
from .template import IMessageTemplate
from viperlog.util.json_util import to_jsonable

class JsonStringFormatter(BaseFormatter[str]):
    def __init__(self, template:Optional[str|IMessageTemplate] = None, helper:Optional[DictFormatter]=None):
        """
        Formats the logrecord into a json string
        Specify either a template or a helper to aid in the formatting
        :param template:
        :param helper:
        """
        super().__init__()
        self._helper = helper or DictFormatter(template)


    def format(self, record: LogRecord) -> str:
        # call dict_formatter to keep creating the props the same for most
        result = self._helper.format(record)
        return json.dumps(result, default=to_jsonable)
