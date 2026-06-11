from abc import ABC, abstractmethod
import unittest

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class TestShape(unittest.TestCase):
    def test_shape_area(self):
        class Circle(Shape):
            def __init__(self, radius):
                self.radius = radius
            
            def area(self):
                return 3.14 * (self.radius ** 2)
        
        circle = Circle(10)
        self.assertEqual(circle.area(), 314)

unittest.main(argv=[''], exit=False)
# Fungsi: Menggunakan unittest untuk menguji implementasi kelas abstrak.
# Kondisi: Ketika Anda ingin memastikan kelas abstrak berfungsi dengan baik dalam konteks unit testing.