
from typing import Optional, Union, List, Dict, Any
from logging import FATAL, NOTSET
from .types import LoggingType, ProcessorsType, FiltersType
from .handlers.viperhandler import ViperHandler
from .viperlog import ViperLog
from .processors.base import IProcessor, BaseProcessor
from .filters.base import IFilter



#from functools import partial
#setup_viperlog_handler = partial(ViperLog.setup_handler, ViperLog())

def setup_viperlog_handler(name:str, logger:Optional[LoggingType|List[LoggingType]] = None, processors:Optional[ProcessorsType|List[ProcessorsType]] = None, filters: Optional[FiltersType|List[FiltersType]] = None, min_level: int = NOTSET,
                     batch_size: int = 100, flush_level: int = FATAL, extra:Optional[Dict[str,Any]] = None)->ViperHandler:
    manager = ViperLog()
    return manager.setup_handler(name=name, logger=logger, processors=processors, filters=filters, min_level=min_level, batch_size=batch_size, flush_level=flush_level, extra=extra)
