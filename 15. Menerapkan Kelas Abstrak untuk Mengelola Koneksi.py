from abc import ABC, abstractmethod

class NetworkConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

class WiFiConnection(NetworkConnection):
    def connect(self):
        return "Connected to WiFi."

class EthernetConnection(NetworkConnection):
    def connect(self):
        return "Connected through Ethernet."

wifi = WiFiConnection()
ethernet = EthernetConnection()

print(wifi.connect())
print(ethernet.connect())
# Fungsi: Mengelola koneksi menggunakan kelas abstrak untuk antarmuka yang bersih.
# Kondisi: Ketika Anda ingin mengatur pengelolaan koneksi ke berbagai sumber daya jaringan.