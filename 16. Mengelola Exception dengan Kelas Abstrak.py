from abc import ABC, abstractmethod

class CustomException(ABC):
    @abstractmethod
    def message(self):
        pass

class NotFoundException(CustomException):
    def message(self):
        return "Not Found Exception Occurred."

exception = NotFoundException()
print(exception.message())
# Fungsi: Mengelola exception menggunakan kelas abstrak untuk antarmuka yang bersih.
# Kondisi: Ketika Anda perlu mendefinisikan jenis-jenis exception dengan perilaku khusus.