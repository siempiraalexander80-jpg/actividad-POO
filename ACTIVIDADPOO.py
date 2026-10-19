# 1 clases y objetos
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")

moto = Vehiculo("Suzuki", "DR 150")
moto.mostrar_info()

# 2 Herencia
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def arrancar(self):
        print("El vehículo está arrancando.")

class Moto(Vehiculo):
    def __init__(self, marca, cilindraje):
        super().__init__(marca)
        self.cilindraje = cilindraje

moto = Moto("Suzuki", 150)

print(moto.marca)
print(moto.cilindraje)
moto.arrancar()

# 3 Polimorfismo
class Moto:
    def arrancar(self):
        print("La moto arranca con su botón.")

class Carro:
    def arrancar(self):
        print("El carro arranca con su llave.")

def iniciar_vehiculo(vehiculo):
    vehiculo.arrancar()

moto = Moto()
carro = Carro()

iniciar_vehiculo(moto)
iniciar_vehiculo(carro)

# 4 Encapsulamiento
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print("Depósito realizado.")
        else:
            print("Monto inválido.")
    @property
    def saldo(self):
        return self.__saldo
cuenta = CuentaBancaria("Carlos", 5000)
cuenta.depositar(1000)
print("Titular:", cuenta.titular)
print("Saldo:", cuenta.saldo)
