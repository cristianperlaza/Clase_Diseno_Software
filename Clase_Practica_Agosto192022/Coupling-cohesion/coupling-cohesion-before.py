import string
import random

class RegistroVehiculo:

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"


class Aplicacion:

    def register_vehicle(self, marca: string):
        # create a registro instance
        registro = RegistroVehiculo()

        # generate a vehicle id of length 12
        vehicle_id = registro.generate_vehicle_id(12)

        # now generate a license plate for the vehicle
        # using the first two characters of the vehicle id
        placa = registro.generate_vehicle_license(vehicle_id)

        # compute the catalogue price
        catalogo_precio = 0
        if marca == "Tesla Model 3":
            catalogo_precio = 60000
        elif marca == "Volkswagen ID3":
            catalogo_precio = 35000
        elif marca == "BMW 5":
            catalogo_precio = 45000

        # compute the tax percentage (default 5% of the catalogue price, except for electric cars where it is 2%)
        porcentaje_impuestos = 0.05
        if marca == "Tesla Model 3" or marca == "Volkswagen ID3":
            porcentaje_impuestos = 0.02

        # compute the payable tax
        impuesto_a_pagar = porcentaje_impuestos * catalogo_precio

        # print out the vehicle registration information
        print("Registration complete. Vehicle information:")
        print(f"marca: {marca}")
        print(f"Id: {vehicle_id}")
        print(f"License plate: {placa}")
        print(f"Payable tax: {impuesto_a_pagar}")

app = Aplicacion()
app.register_vehicle("Volkswagen ID3")