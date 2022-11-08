from serverlet import serverlet
from battery.NubbinBattery import NubbinBattery
from battery.SpindlerBattery import SpindlerBattery
from car import Car
from engine.CapuletEngine import CapuletEngine
from engine.SternmanEngine import SternmanEngine
from engine.WilloughbyEngine import WilloughbyEngine
#import utils
from carFactory import carFactory
import datetime
new_car=carFactory.create_calliope(datetime.datetime(2022, 5, 18),datetime.datetime(2020, 5, 17),15,15)
print(new_car.needs_service())