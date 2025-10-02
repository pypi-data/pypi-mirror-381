from pdi.Signalling.Event.AbstractEvent import Event


class ClientExecuteError(Event):
    def __init__(self, exception: Exception, code: str):
        self.exception = exception
        self.code = code

    @classmethod
    def getName(cls) -> str:
        return 'client:execute:error'
