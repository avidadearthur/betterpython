from time import sleep
from VehicleInfo import VehicleInfo
import random
import string

class Vehicle:
    id: str
    license_plate: str
    info: VehicleInfo

    def __init__(self, info: VehicleInfo):
        self.id = self.generate_vehicle_id(12)
        self.license_plate = self.generate_vehicle_license(self.id)
        self.info = info

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def print(self):
        print(f"Id: {self.id}")
        print(f"License plate: {self.license_plate}")
        self.info.print()
