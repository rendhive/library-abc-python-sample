from abc import ABC, abstractmethod

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rectangle = Rectangle(5, 10)
print("Area of rectangle:", rectangle.area())
# Fungsi: Mengimplementasikan metode abstrak di kelas turunan.
# Kondisi: Ketika Anda ingin menambahkan logika ke metode abstrak pada subkelas.