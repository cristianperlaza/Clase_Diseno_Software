import string
import random

class InformacionVehiculo:
    
    def __init__(self, marca, electrico, catalogo_precio):
        self.marca = marca
        self.electrico = electrico
        self.catalogo_precio = catalogo_precio

    def compute_tax(self):
        tax_percentage = 0.05
        if self.electrico:
            tax_percentage = 0.02
        return tax_percentage * self.catalogo_precio

    def print(self):
        print(f"marca: {self.marca}")
        print(f"Payable tax: {self.compute_tax()}")

class Vehiculo:

    def __init__(self, id, placa, info):
        self.id = id
        self.placa = placa
        self.info = info

    def print(self):
        print(f"Id: {self.id}")
        print(f"License plate: {self.placa}")
        self.info.print()


class RegistroVehiculo:

    def __init__(self):
        self.vehicle_info = { }
        self.add_vehicle_info("Tesla Model 3", True, 60000)
        self.add_vehicle_info("Volkswagen ID3", True, 35000)
        self.add_vehicle_info("BMW 5", False, 45000)
        self.add_vehicle_info("Tesla Model Y", True, 75000)

    def add_vehicle_info(self, marca, electrico, catalogo_precio):
        self.vehicle_info[marca] = InformacionVehiculo(marca, electrico, catalogo_precio)

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, marca):
        id = self.generate_vehicle_id(12)
        placa = self.generate_vehicle_license(id)
        return Vehiculo(id, placa, self.vehicle_info[marca])


class Applicacion:

    def register_vehicle(self, marca: string):
        # create a registry instance
        registry = RegistroVehiculo()

        vehicle = registry.create_vehicle(marca)

        # print out the vehicle information
        vehicle.print()

app = Applicacion()
app.register_vehicle("Tesla Model Y")