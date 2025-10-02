from pdi.Signalling.Event.AbstractEvent import Event


class ApplicationInitializing(Event):
    @classmethod
    def getName(cls) -> str:
        return 'application:initializing'


class ApplicationStarted(Event):
    @classmethod
    def getName(cls) -> str:
        return 'application:started'


class ApplicationExit(Event):
    @classmethod
    def getName(cls) -> str:
        return 'application:exit'

class HideIndicator(Event):
    @classmethod
    def getName(cls) -> str:
        return 'indicator:hide'


class ShowIndicator(Event):
    @classmethod
    def getName(cls) -> str:
        return 'indicator:show'


class AudioInputDisable(Event):
    @classmethod
    def getName(cls) -> str:
        return 'input:audio:disable'


class AudioInputEnable(Event):
    @classmethod
    def getName(cls) -> str:
        return 'input:audio:enable'


class AudioOutputDisable(Event):
    @classmethod
    def getName(cls) -> str:
        return 'output:audio:disable'


class AudioOutputEnable(Event):
    @classmethod
    def getName(cls) -> str:
        return 'output:audio:enable'
