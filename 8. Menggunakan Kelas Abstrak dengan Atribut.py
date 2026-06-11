from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def vehicle_type(self):
        pass

class Car(Vehicle):
    def vehicle_type(self):
        return "Car"

class Truck(Vehicle):
    def vehicle_type(self):
        return "Truck"

car = Car()
truck = Truck()
print(car.vehicle_type(), "and", truck.vehicle_type())
# Fungsi: Menggunakan kelas dan metode abstrak untuk mendeskripsikan tipe kendaraan.
# Kondisi: Ketika Anda perlu mengembangkan berbagai tipe kendaraan dengan interaksi umum.