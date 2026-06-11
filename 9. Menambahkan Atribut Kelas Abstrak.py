from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self) -> str:
        pass

class Dog(Animal):
    def sound(self) -> str:
        return "Woof!"

dog = Dog()
print("Dog sound:", dog.sound())
# Fungsi: Kelas abstrak dengan metode untuk mendeskripsikan suara hewan.
# Kondisi: Ketika Anda memiliki berbagai jenis hewan dengan perilaku yang berbeda.