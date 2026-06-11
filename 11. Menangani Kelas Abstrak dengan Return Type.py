from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Square(Shape):
    def __init__(self, side_length: float):
        self.side_length = side_length

    def area(self) -> float:
        return self.side_length ** 2

square = Square(4)
print("Area of square:", square.area())
# Fungsi: Menentukan tipe pengembalian metode abstrak.
# Kondisi: Ketika Anda ingin membatasi jenis data yang dikembalikan oleh metode.