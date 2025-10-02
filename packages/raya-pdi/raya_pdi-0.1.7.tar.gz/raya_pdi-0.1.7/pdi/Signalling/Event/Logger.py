from abc import ABC

from pdi.Signalling.Event.AbstractEvent import Event


class Logger(Event, ABC):
    def __init__(self, message: str):
        self.message = message


class LoggerError(Logger):
    @classmethod
    def getName(cls) -> str:
        return 'logger:error'


class LoggerInfo(Logger):
    @classmethod
    def getName(cls) -> str:
        return 'logger:info'


class LoggerDebug(Logger):
    @classmethod
    def getName(cls) -> str:
        return 'logger:debug'
