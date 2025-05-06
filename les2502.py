from distutils.dist import command_re

from sqlalchemy import create_engine, Column, Integer, String, Sequence, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import text
import json

#
# with open('config.json', 'r') as file:
#     data = json.load(file)
#     login = data['login']
#     password = data ['password']
#
#     db_url = f"postgresql+pg8000://{login}:{password}@localhost:5432/itstep"
# engine = create_engine(db_url)
#
# Base = declarative_base()
#
# # class User(Base):
# #     __tablename__ = 'users'
# #
# #     id = Column(Integer, Sequence('user_id_seg'), primary_key=True)
# #     name = Column(String(30))
# #     city = Column(String(50))
#
#     def __repr__(self):
#         return f"User(id={self.id}, name={self.name}, city={self.city})"
#
#
# #обавити таблицю у базу даних
# Base.metadata.create_all(engine)
#
# #створюэмо юзерив
# Session = sessionmaker(bind=engine)
# session = Session()
#
# user1 = User(name='Jhon', city='LA')
# user2 = User(name='Sophia', city='London')
#
# users = [user1, user2]
# session.add_all(users)
#
# session.commit()
#
#
# # показати усі рядки таблиці(через session)
# rows = session.query(User).all()
#
# # for row in rows:
# #     print(row)
# #
# # # показати усі рядки таблиці(через SQL)
# # запит як str
# query = """
# SELECT *
# FROM USERS
# """
#
# query_sql = text(query)
#
# # виконуємо запит
# result = session.execute(query_sql)
# rows = result.fetchall()
#
# # for row in rows:
# #     print(type(row))
# #     print(row)

#
# Завдання 1
# Створіть однотабличну базу даних People (ім’я, прізвище, місто, країна, дата народження) з однойменною
# таблицею. Напишіть програму, яка дозволяє користувачеві ввести запит і отримати результати роботи запиту.
# Підтримуйте лише SELECT як запит. Якщо ви спробуєте
# виконати інші запити, потрібно буде генерувати помилку.
# Завдання 2
# Додайте до першого завдання можливість вносити,
# видаляти, оновлювати дані за допомогою запитів INSERT,
# DELETE, UPDATE. Перед виконанням запиту перевіряйте
# правильність назви таблиці. Також забороніть запит на
# видалення та оновлення усіх рядків (UPDATE та DELETE
# без умов).
# Завдання 3
# Модифікуйте перше завдання так, щоб користувач не
# міг вводити запит, а користувався готовими фільтрами.
# Наприклад: відображення усіх людей, відображення усіх
# людей з одного
# Практичне завдання
# 1
# міста (користувач задає з клавіатури як значення), відображення усіх людей з однієї країни (користувач задає з
# клавіатури як параметр).
# Завдання 4
# Модифікуйте третє завдання, щоб фільтр для показу міг бути комплексним. Наприклад, користувач може
# виставити фільтр на країну та місто, після чого відобразяться люди, для яких спрацює цей комплексний
# фільтр. Підтримайте умову АБО.
# Завдання 5
# Додайте до четвертого завдання можливість вносити,
# видаляти, оновлювати дані через інтерфейс додатка. Користувач не може ввести запит INSERT, UPDATE, DELETE
# безпосередньо.
# Завдання 6
# Додайте до додатку можливість зберігати результати
# роботи фільтрів у файл. Наприклад, результат роботи
# фільтра для відображення усіх людей або результат роботи
# фільтра з відображення людей з одного міста.



# Створіть однотабличну базу даних People (ім’я, прізвище, місто, країна, дата народження) з однойменною
# таблицею. Напишіть програму, яка дозволяє користувачеві ввести запит і отримати результати роботи запиту.
# Підтримуйте лише SELECT як запит. Якщо ви спробуєте
# виконати інші запити, потрібно буде генерувати помилку.
# with open('config.json', 'r') as file:
#     data = json.load(file)
#     login = data['login']
#     password = data ['password']
#
#     db_url = f"postgresql+pg8000://{login}:{password}@localhost:5432/people"
# engine = create_engine(db_url)
#
# Base = declarative_base()
#
# class People(Base):
#     __tablename__ = 'peole'
#     id = Column(Integer, Sequence('user_id_seg'), primary_key=True)
#     name = Column(String(20))
#     surname = Column(String(20))
#     city = Column(String(20))
#     country = Column(String(20))
#     date_dr = Column(Date)
#
#
#     def __repr__(self):
#         return (f"id = {self.id}, name = {self.name}, surname = {self.surname}, city = {self.city}, "
#                 f"country = {self.country}, date_dr = {self.date_dr} ")
#
# Base.metadata.create_all(engine)
#
# from datetime import date
#
# people_list = [
#     People(name="Олександр", surname="Шевченко", city="Київ", country="Україна", date_dr=date(1990, 5, 15)),
#     People(name="Ірина", surname="Коваленко", city="Харків", country="Україна", date_dr=date(1985, 3, 10)),
#     People(name="Андрій", surname="Мельник", city="Львів", country="Україна", date_dr=date(1993, 7, 8)),
#     People(name="Світлана", surname="Іванова", city="Одеса", country="Україна", date_dr=date(1992, 1, 21)),
#     People(name="Віктор", surname="Петренко", city="Дніпро", country="Україна", date_dr=date(1988, 9, 30)),
#     People(name="Марія", surname="Гриценко", city="Запоріжжя", country="Україна", date_dr=date(1995, 11, 5)),
#     People(name="Євген", surname="Сидоренко", city="Полтава", country="Україна", date_dr=date(1989, 6, 12)),
#     People(name="Анна", surname="Ткаченко", city="Чернігів", country="Україна", date_dr=date(1991, 2, 28)),
#     People(name="Дмитро", surname="Кузьменко", city="Вінниця", country="Україна", date_dr=date(1994, 4, 17)),
#     People(name="Олена", surname="Литвин", city="Івано-Франківськ", country="Україна", date_dr=date(1987, 8, 23))
# ]
#
# Session = sessionmaker(engine)
# session = Session()
# session.add_all(people_list)
# session.commit()
#
# def command1():
#     user_inp = input('введіть запит: ')
#
#     query_sql = text(user_inp)
#
#     # виконуємо запит
#     result = session.execute(query_sql)
#     rows = result.fetchall()
#
#     for row in rows:
#         print(row)
#
# while True:
#     print('1 - виконати запит')
#     command = input('введіть номер команди: ')
#
#     if command == '1':
#         command1()
#
#     else:
#
#
# import redis
#
# server = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
#
# server.set('user:name', 'Антон')
#
# name = server.get('user:name')
# print(name)
#
# import redis
#
# class RedisCart:
#
#     def __init__(self):
#         self.server = redis.Redis(
#             host='localhost' ,
#             port=6379,
#             db=0,
#             decode_responses=True
#         )
#         self.current_user = None
#
#
#     def
#
#     def register_user(self, username, password):
#
#         if self.server.hexists('users', username):
#             print('користувач вже зареєстрований!')
#             return
#
#
#         self.server.hset(
#             'users',
#             username,
#             password
#         )
#
#     def login(self, username, password):
#
#         if not self.server.hexists('users', username):
#             print("невірне імя!")
#             return
#
#         real_password = self.server.hget(
#             "users", username
#         )
#         if real_password == password:
#             print('доступ надано')
#             self.current_user = username
#         else:
#             print("невірний пароль")
#
#
#     def add_item(self, item_id, item_count):
#         # cats:username = {
#         #     "item_id": count
#         # }
#         #
#
#         if self.current_user is None:
#             print('потрібно залогінитись')
#             return
#
#
#         key = f"carts:{self.current_user}"
#
#         if self.server.hexists(key, item_id):
#             old_count = self.server.hget(key, item_id)
#             new_count = old_count + item_count
#         self.server.hset(key, item_id, item_count)
#
#         else:
#             self.server.hset(key, item_id, item_count)
#
#
# cart = RedisCart()
# while True:
#     print('0 -- вихід')
#     print('1 -- реєстрація нового користувача')
#     print('2 -- логін')
#     print('3 -- додати товар до кошика')
#     command = input('введіть номер команди')
#
#     if command == '0':
#         break
#     elif command == '1':
#         username = input('введіть імя користувача: ')
#         password = input('введіть пароль: ')
#         cart.register_user(username, password)
#
#
#     elif command == '2':
#         username = input('введіть імя користувача: ')
#         password = input('введіть пароль: ')
#         cart.login(username, password)
#
#     elif command == '3':
#         item_id = input('введіть ід товару: ')
#         count = input('введіть кі-ть: ')
#         cart.add_item(item_id, count)
#
#     else:
#         print('невірна команда')
#



# екзамен!!!!!!!!

# 1. Напишіть програму, яка приймає два цілих числа від
# користувача і виводить суму діапазону чисел між ними.

# num1 = int(input('введіть число: '))
# num2 = int(input('ведіть друге число: '))
#
# print('Сума чисел в  діапазоні: ', sum(range(min(num1, num2) + 1, max(num1, num2))))


# 2. Напишіть програму, для знаходження суми всіх парних
# чисел від 1 до 100.

# suma = 0
#
# for i in range(1, 101):
#
#     if i % 2 == 0:
#         suma = suma + i
#
# print("Сума парних чисел від 1 до 100:", suma)


# 3. Напишіть програму, яка приймає рядок від користувача і
# виводить кожну літеру рядка на окремому рядку.

# user_text = input("Введіть рядок: ")
# for char in user_text:
#     print(char)

# 4. Напишіть програму, яка створює список цілих чисел та
# виводить новий список, який містить лише парні числа з
# вихідного списку.

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_num = []
#
# for num in nums:
#     if num % 2 == 0:
#         even_num.append(num)
#
# print("Парні числа:", even_num)

# 5. Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, що починаються з великої літери.

# lists = ["Привіт", "hello", "Світ", "python"]
# new = []
#
# for list in lists:
#     if list[0].isupper():
#        new.append(list)

# print("Рядки з великої букви:", new)


# 6. Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, які містять слово "Python".

# user_input = input('введіть рядки через кому: ')
# user_list = user_input.split(",")
# new_list = []
#
# for line in user_list:
#     if "Python" in line:
#         new_list.append(line)
# print("Рядки з 'Python':", new_list)

# 7. (додаткове на кристалики)Напишіть програму, яка
# створює словник, де ключами є слова, а значеннями - їхні
# визначення. Дозвольте користувачу додавати, видаляти
# та шукати слова у цьому словнику.

# dictionary = {}
#
# def add_word():
#     word = input("введіть слово: ")
#     definition = input("введіть визначення: ")
#     dictionary[word] = definition
#     print(f"слово '{word}' додано до словника!")
#
#
# def delete_word():
#     word = input("введіть слово для видалення: ")
#     if word in dictionary:
#         del dictionary[word]
#         print(f"слово '{word}' видалено!")
#     else:
#         print(f"слово '{word}' не знайдено!")
#
#
# def search_word():
#     word = input("введіть слово для пошуку: ")
#     if word in dictionary:
#         print(f"визначення слова '{word}': {dictionary[word]}")
#     else:
#         print(f"слово '{word}' не знайдено!")
#
#
# def menu():
#     while True:
#         print("\nМеню:")
#         print("1. Додати слово")
#         print("2. Видалити слово")
#         print("3. Пошук слова")
#         print("4. Вийти")
#
#         choice = input("Виберіть опцію (1-4): ")
#
#         if choice == '1':
#             add_word()
#         elif choice == '2':
#             delete_word()
#         elif choice == '3':
#             search_word()
#         elif choice == '4':
#             print("До побачення!")
#             break
#         else:
#             print("невірний вибір.")
#
# menu()

# Частина 2: Об'єктно-орієнтоване програмування (ООП)
# Симулятор роботи сайту
# WebSite: Основний клас, який представляє вебсайт.
# Атрибути: назва сайту, URL, список сторінок.
# Методи: додавання/видалення сторінок, відображення
# інформації про сайт.
# WebPage: Клас, який представляє окрему сторінку на сайті.
# Атрибути: заголовок сторінки, вміст, дата публікації.
# Методи: відображення деталей сторінки.
# Реалізація функціональності:
# Дозвольте користувачеві створювати новий сайт з
# певною назвою та URL. Додайте можливість створювати нові
# сторінки для сайту, вводячи заголовок та вміст. Реалізуйте
# функцію для видалення сторінок з сайту. Включіть функцію
# для відображення всієї інформації про сайт, включаючи
# список усіх сторінок.
# Розробіть простий текстовий інтерфейс для взаємодії з
# користувачем. Користувач повинен мати змогу вибирати дії,
# такі як створення сайту, додавання/видалення сторінок,
# перегляд інформації про сайт.
# #
# import datetime
#
# class WebPage:  #сторінка на сайті
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#         self.date_published = datetime.datetime.now()
#
#     def show_details(self):
#         print(f"Заголовок: {self.title}")
#         print(f"Вміст: {self.content}")
#         print(f"Дата публікації: {self.date_published.strftime('%Y-%m-%d %H:%M:%S')}")
#
#
# class WebSite:
#     def __init__(self, name, url):
#         self.name = name
#         self.url = url
#         self.pages = []
#
#     def add_page(self, page):
#         self.pages.append(page)
#
#     def delete_page(self, title):
#         self.pages = [page for page in self.pages if page.title != title]
#
#     def show_info(self):
#         print(f"\nсайт: {self.name} ({self.url})")
#         print("сторінки:")
#         for page in self.pages:
#             print(f" - {page.title}")
#
#
# def main():
#     website = None
#
#     while True:
#         print("\n1. Створити сайт")
#         print("2. Додати сторінку")
#         print("3. Видалити сторінку")
#         print("4. Переглянути інформацію про сайт")
#         print("5. Вийти")
#
#         choice = input("оберіть дію: ")
#
#         if choice == "1":
#             # перевірка на існуючий сайт
#             if website:
#                 print("сайт вже існує. вийдіть або видаліть сайт.")
#             else:
#                 name = input("Введіть назву сайту: ")
#                 url = input("Введіть URL сайту: ")
#                 website = WebSite(name, url)
#                 print(f"сайт '{name}' створено.")
#
#         elif choice == "2" and website:
#             # перевірка на існуючий сайт
#             title = input("Введіть заголовок сторінки: ")
#             content = input("Введіть вміст сторінки: ")
#             page = WebPage(title, content)
#             website.add_page(page)
#             print(f"сторінка '{title}' додана.")
#
#         elif choice == "2" and not website:
#             print("створіть сайт, щоб додавати сторінки.")
#
#         elif choice == "3" and website:
#             # меревірка на наявність сторінки
#             title = input("Введіть заголовок сторінки для видалення: ")
#             found = False
#             for page in website.pages:
#                 if page.title == title:
#                     website.delete_page(title)
#                     print(f"Сторінка '{title}' видалена.")
#                     found = True
#                     break
#             if not found:
#                 print(f"сторінка з заголовком '{title}' не знайдена.")
#
#         elif choice == "3" and not website:
#             print("створіть сайт, щоб видаляти сторінки.")
#
#         elif choice == "4" and website:
#             website.show_info()
#             if website.pages:
#                 for page in website.pages:
#                     print("\nІнфо про сторінку:")
#                     page.show_details()
#             else:
#                 print("Немає сторінок на сайті.")
#
#         elif choice == "4" and not website:
#             print("сайт ще не створений.")
#
#         elif choice == "5":
#             print("Вихід з програми...")
#             break
#         else:
#             print("Невірна дія або спочатку створіть сайт.")
#
# if __name__ == "__main__":
#     main()

