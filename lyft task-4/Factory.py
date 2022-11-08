from battery.NubbinBattery import NubbinBattery
from battery.SpindlerBattery import SpindlerBattery
from car import Car
from engine.CapuletEngine import CapuletEngine
from engine.SternmanEngine import SternmanEngine
from engine.WilloughbyEngine import WilloughbyEngine
from tires.Octoprime_tires import Octoprime
from tires.Carrigan_tires import Carrigan
class carFactory: 
   @staticmethod
   def create_calliope(current_date, last_service_date, current_mileage,last_service_mileage,wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = Carrigan(wear)
        car = Car(engine, battery,tires)
        return car

   @staticmethod
   def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage,wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = Octoprime(wear)
        car = Car(engine, battery,tires)
        return car

   @staticmethod
   def create_palindrome(current_date, last_service_date,wear,warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = Carrigan(wear)
        car = Car(engine, battery,tires)
        return car

   @staticmethod
   def create_rorschach(current_date, last_service_date, current_mileage,last_service_mileage,wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = Octoprime(wear)
        car = Car(engine, battery,tires)
        return car

   @staticmethod
   def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage,wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = Carrigan(wear)
        car = Car(engine, battery,tires)
        return car
