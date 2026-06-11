from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @staticmethod
    def define_shape():
        return "This is a shape."

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

print(Circle.define_shape())  # Memanggil metode statik dari kelas abstrak
# Fungsi: Menambahkan metode statik ke dalam kelas abstrak.
# Kondisi: Ketika Anda ingin mendefinisikan perilaku kelas yang bersifat umum tanpa bergantung pada instance.