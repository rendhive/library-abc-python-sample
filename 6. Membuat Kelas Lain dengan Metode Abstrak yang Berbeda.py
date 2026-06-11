from abc import ABC, abstractmethod

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

circle = Circle(3)
print("Area of circle:", circle.area())
# Fungsi: Mengimplementasikan kelas lain yang juga mewarisi dari Shape.
# Kondisi: Ketika Anda ingin menyoroti fleksibilitas desain kelas-konsep yang sama.