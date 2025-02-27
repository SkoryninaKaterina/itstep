# Завдання 1
# Створіть наступні класи:
#  CreditCardPayment – атрибути currency
#  PayPalPayment – атрибути currency
#  CryptoPayment – атрибути currency
# Методи:
#  pay(amount) – виводить повідомлення
# o CreditCardPayment – оплата карткою {amount}{currency}
# o PayPalPayment – оплата PayPal {amount}{currency}
# o CryptoPayment – оплата криптогаманцем {amount}{currency}
# Напишіть функцію create_payment() яка запитує у
# користувача тип рахунку та потрібні атрибути і повертає
# об’єкт.
# Створіть декілька рахунків, добавте їх у список та для
# кожної викличте відповідні методи.

class Payment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Оплата карткою {amount} {self.currency}")


class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Оплата PayPal {amount} {self.currency}")


class CryptoPayment(Payment):
    def pay(self, amount):
        print(f"Оплата криптогаманцем {amount} {self.currency}")


def create_payment():
    payment_type = input("Введіть тип рахунку (CreditCard, PayPal, Crypto): ").strip()
    currency = input("Введіть валюту: ").strip()

    payment_classes = {
        "CreditCard": CreditCardPayment,
        "PayPal": PayPalPayment,
        "Crypto": CryptoPayment
    }

    if payment_type not in payment_classes:
        print("Невідомий тип платежу!")
        return None

    return payment_classes[payment_type](currency)



payments = []
for i in range(3):
    payment = create_payment()
    if payment:
        payments.append(payment)


for payment in payments:
    amount = float(input(f"Введіть суму для {payment.__class__.__name__}: "))
    payment.pay(amount)




