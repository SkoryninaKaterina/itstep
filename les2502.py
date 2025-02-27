# Завдання 1
# Напишіть клас Банківський рахунок з атрибутами:
#  ім'я клієнта
#  баланс
#  валюта
#  словник з курсом валют(однаковий для всіх)
# Додайте методи:
#  вивід загальної інформації
#  перевірка чи відома валюта(якщо ні, викликати
# ValueError)
#  перевести гроші з однієї валюти в іншу(ця операція
# часто використовується, тому зрочно реалізувати
# окремим методом)
#  зміна валюти
#  поповнення балансу(валюта та сама)
#  зняття грошей з балансу(валюта та сама).



class BankAccount:
    exchange_rates = {'USD': 1, 'EUR': 0.85, 'UAH': 28.3}

    def __init__(self, client_name, balance, currency):
        if currency not in self.exchange_rates:
            raise ValueError('Unknown currency')
        self.client_name = client_name
        self.balance = balance
        self.currency = currency

    def __str__(self):
        return f'Client: {self.client_name}, balance: {self.balance:.2f}, currency: {self.currency}'

    def check_currency(self, currency):

        if currency not in self.exchange_rates:
            raise ValueError(f'Unknown currency: {currency}')

    def convert_currency(self, to_currency):

        self.check_currency(to_currency)
        self.balance = self.balance * self.exchange_rates[to_currency] / self.exchange_rates[self.currency]
        self.currency = to_currency

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError('Amount must be positive')
        self.balance += amount

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError('Amount must be positive')
        if amount > self.balance:
            raise ValueError('Not enough money')
        self.balance -= amount

    def info(self):
        print(self)


account = BankAccount('John', 100, 'USD')
print(account)
account.convert_currency('EUR')
print(account)
account.deposit(100)
print(account)
account.withdraw(50)
print(account)
account.info()


