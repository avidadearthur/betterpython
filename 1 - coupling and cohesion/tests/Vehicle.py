from time import sleep
from VehicleInfo import VehicleInfo

class Vehicle:
    id: str
    license_plate: str
    info: VehicleInfo

    def __init__(self, id: str, license_plate: str, info: VehicleInfo):
        self.id = id
        self.license_plate = license_plate
        self.info = info


    def print(self):
        print(f"Id: {self.id}")
        print(f"License plate: {self.license_plate}")
        self.info.print()
