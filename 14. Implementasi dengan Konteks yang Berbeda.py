from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class PayPalProcessor(PaymentProcessor):
    def pay(self, amount: float):
        return f"Paid {amount} using PayPal."

class CreditCardProcessor(PaymentProcessor):
    def pay(self, amount: float):
        return f"Paid {amount} using Credit Card."

paypal = PayPalProcessor()
cc = CreditCardProcessor()

print(paypal.pay(100))
print(cc.pay(200))
# Fungsi: Mendesain pengolahan pembayaran melalui kelas abstrak.
# Kondisi: Ketika Anda memerlukan integrasi berbagai jenis pembayaran.