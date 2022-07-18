from Vehicle import Vehicle
from VehicleInfo import VehicleInfo
import random, string, json

class VehicleRegistry:
    data: dict

    def __init__(self):
        # TODO 3 - put vehicle info in JSON file
        self.vehicle_info = { }
        self.add_vehicle_info("Tesla Model 3", True, 60000)
        self.add_vehicle_info("Volkswagen ID3", True, 35000)
        self.add_vehicle_info("BMW 5", False, 45000)
        self.add_vehicle_info("Tesla Model Y", True, 75000)


    def create_vehicle(self, brand):
        id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(id)

        with open("C:/Users/arthu/VSCodeProjects/betterpython/1 - coupling and cohesion/tests/data.json", "r+") as jsonFile:
            self.data = json.load(jsonFile)

            self.data[id] = [license_plate, self.vehicle_info[brand].to_string()]

            jsonFile.seek(0)  # rewind
            jsonFile.write(json.dumps(self.data))
            jsonFile.truncate()
        
        jsonFile.close()

        return Vehicle(id, license_plate, self.vehicle_info[brand])

    # TODO 4 - maybe move this to VehicleInfo 
    def add_vehicle_info(self, brand, electric, catalogue_price):
        self.vehicle_info[brand] = VehicleInfo(brand, electric, catalogue_price)

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"
