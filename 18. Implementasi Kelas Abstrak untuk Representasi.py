from abc import ABC, abstractmethod

class Representation(ABC):
    @abstractmethod
    def display(self):
        pass

class TextDisplay(Representation):
    def display(self):
        return "Displaying text"

class ImageDisplay(Representation):
    def display(self):
        return "Displaying image"

text = TextDisplay()
print(text.display())

image = ImageDisplay()
print(image.display())
# Fungsi: Mengelola representasi data dengan kelas abstrak untuk fleksibilitas.
# Kondisi: Ketika Anda ingin merepresentasikan berbagai bentuk data dalam proyek.