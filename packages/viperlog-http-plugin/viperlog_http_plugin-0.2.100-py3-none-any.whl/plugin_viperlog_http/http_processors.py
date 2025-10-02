import logging
from logging import LogRecord
from typing import List, Optional, Dict, Any
from viperlog.formatters import BaseFormatter, DictFormatter
from viperlog.formatters.base import BaseFormatter
from viperlog.formatters.dict_formatter import DictFormatter

#from viperlog.processors import BaseProcessor, GenericProcessor
from viperlog.processors.base_generic import GenericProcessor

from logging import getLogger
import httpx



# prevent logging from bubbling up and causing loops

class HttpxLoggingContext:
    def __init__(self) -> None:
        self._loggers = [getLogger("httpx"), getLogger("httpcore")]
        self._propagate = [x.propagate for x in self._loggers]


    def __enter__(self):
        # disable propagation
        for x in self._loggers:
            x.propagate=False
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # restore propagation property
        for i in range(0, len(self._loggers)):
            self._loggers[i].propagate = self._propagate[i]

class HttpProcessor(GenericProcessor[Dict[str, Any]]):

    def __init__(self, url:str, formatter:Optional[BaseFormatter[Dict[str, Any]]]=DictFormatter()):
        super().__init__(formatter)
        self._url = url
        self._client = httpx.Client()

    def process_messages(self, records: List[Dict[str, Any]]) -> None:
        body = records
        #self._client.post(self._url, json = body)
        self.do_post(self._url, json = body)

    def do_post(self, url:str, json:Any)->None:
        # prevent propagation of the httpx logging so we don't get loops
        with HttpxLoggingContext() as ctx:
            self._client.post(url, json=json)



#class HttpProcessor(BaseProcessor):
#    def __init__(self, url:str):
#        super().__init__()
#        self._url = url
#        self._formatter = DictFormatter()#
#
#    def process_records(self, records: List[LogRecord]) -> None:
#        body = [self._formatter.format(r) for r in records]
#        httpx.post(self._url, json = body)


