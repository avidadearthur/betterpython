from time import sleep
from VehicleInfo import VehicleInfo

class Vehicle:
    id: str
    license_plate: str
    info: VehicleInfo

    def __init__(self, info: VehicleInfo):
        self.id = self.generate_vehicle_id(12)
        self.license_plate = self.generate_vehicle_license(self.id)
        self.info = info


    def print(self):
        print(f"Id: {self.id}")
        print(f"License plate: {self.license_plate}")
        self.info.print()
