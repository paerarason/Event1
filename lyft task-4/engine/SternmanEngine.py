from engine.engine import Engine
class SternmanEngine:
    def __init__(self,warning_light_on ):
        self.__warning_light_on=warning_light_on
    def needs_service(self):
        return self.__warning_light_on