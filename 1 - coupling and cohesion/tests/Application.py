from Vehicle import Vehicle
from VehicleInfo import VehicleInfo
import string

class Application:

    def __init__(self):
        # TODO 1 - Separate registry in diferent class
        # TODO 2 - replace by JSON file or DB
        self.vehicle_info = { }
        self.add_vehicle_info("Tesla Model 3", True, 60000)
        self.add_vehicle_info("Volkswagen ID3", True, 35000)
        self.add_vehicle_info("BMW 5", False, 45000)
        self.add_vehicle_info("Tesla Model Y", True, 75000)

    def add_vehicle_info(self, brand, electric, catalogue_price):
        self.vehicle_info[brand] = VehicleInfo(brand, electric, catalogue_price)

    def create_vehicle(self, brand):
        return Vehicle(self.vehicle_info[brand])

    def register_vehicle(self, brand: string):

        vehicle = self.create_vehicle(brand)
        vehicle.print()

app = Application()
app.register_vehicle("Volkswagen ID3")