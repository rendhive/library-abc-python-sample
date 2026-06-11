from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def set_name(self, name: str):
        pass

class Employee(Person):
    def __init__(self):
        self.name = ""

    def set_name(self, name: str):
        self.name = name

emp = Employee()
emp.set_name("Alice")
print("Employee Name:", emp.name)
# Fungsi: Menggunakan metode abstrak untuk mendefinisikan setter.
# Kondisi: Ketika Anda ingin mendefinisikan cara mengatur nama di subclass.