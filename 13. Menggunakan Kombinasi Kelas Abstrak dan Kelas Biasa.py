from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Lion(Animal):
    def make_sound(self):
        return "Roar"

def animal_sound(animal: Animal):
    print(animal.make_sound())

cat = Cat()
lion = Lion()
animal_sound(cat)
animal_sound(lion)
# Fungsi: Menggunakan API untuk berbagai jenis hewan dengan perilaku berbeda.
# Kondisi: Ketika Anda ingin menyederhanakan pengelolaan perilaku hewan dengan antarmuka terstandarisasi.