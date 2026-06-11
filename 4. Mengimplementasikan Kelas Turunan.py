from abc import ABC, abstractmethod

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @abstractmethod
    def area(self):
        return self.width * self.height

rectangle = Rectangle(5, 10)
# Fungsi: Mendefinisikan kelas turunan yang mengimplementasikan metode area.
# Kondisi: Ketika Anda perlu membuat kelas yang memiliki perilaku khusus.