from Vehicle import Vehicle
from VehicleInfo import VehicleInfo
from VehicleRegistry import VehicleRegistry
import string

class Application:

    def register_vehicle(self, brand: string):
        # create a registry instance
        registry = VehicleRegistry()

        vehicle = registry.create_vehicle(brand)
        vehicle.print()

app = Application()
app.register_vehicle("Volkswagen ID3")