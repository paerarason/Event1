from engine.engine import Engine
class CapuletEngine:
    def __init__(self,current_milage,last_service_mileage) :
        self.last_service_mileage=last_service_mileage
        self.current_milage=current_milage
    def needs_service(self):
        if self.current_milage-self.last_service_mileage>30000:
           return True
        return False
