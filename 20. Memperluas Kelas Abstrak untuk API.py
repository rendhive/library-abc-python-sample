from abc import ABC, abstractmethod

class API(ABC):
    @abstractmethod
    def fetch_data(self):
        pass

class DataAPI(API):
    def fetch_data(self):
        return {"data": "sample data"}

api = DataAPI()
print(api.fetch_data())  # Mengambil data menggunakan API
# Fungsi: Membentuk struktur API menggunakan kelas abstrak.
# Kondisi: Ketika Anda ingin memberikan antarmuka umum untuk penggunaan berbagai API.