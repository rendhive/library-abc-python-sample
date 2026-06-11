from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        return "Connecting to MySQL database."

mysql_db = MySQLDatabase()
print(mysql_db.connect())
# Fungsi: Mendesain API dengan menggunakan kelas abstrak untuk berbagai tipe database.
# Kondisi: Ketika Anda ingin mengabstraksikan implementasi yang berbeda dalam pengkabelan.