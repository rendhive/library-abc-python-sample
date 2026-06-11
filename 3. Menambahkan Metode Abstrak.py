from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Fungsi: Menyatakan metode abstrak yang harus diimplementasikan oleh subkelas.
# Kondisi: Ketika Anda ingin memaksa subkelas untuk menyediakan implementasi khusus.