from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

def calculate_area(shape: Shape):
    return shape.area()

rectangle = Rectangle(5, 10)
circle = Circle(3)

print("Rectangle Area:", calculate_area(rectangle))
print("Circle Area:", calculate_area(circle))
# Fungsi: Menggunakan kelas abstrak untuk memberikan antarmuka umum.
# Kondisi: Ketika Anda ingin menerapkan polimorfisme dengan cara yang terstruktur.