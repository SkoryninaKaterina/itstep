# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def __str__(self):
#         return f"{self.brand} {self.model} ({self.year})"
#
#
# class TreeNode:
#     def __init__(self, car):
#         self.car = car
#         self.left = None
#         self.right = None
#
#
# class CarPark:
#     def __init__(self):
#         self.root = None
#         self._size = 0
#
#     def add(self, car):
#         def insert(node, car):
#             if not node:
#                 return TreeNode(car)
#             if car.model < node.car.model:
#                 node.left = insert(node.left, car)
#             else:
#                 node.right = insert(node.right, car)
#             return node
#
#         self.root = insert(self.root, car)
#         self._size += 1
#
#     def _find_min(self, node):
#         while node.left:
#             node = node.left
#         return node
#
#     def remove(self, model):
#         def delete(node, model):
#             if not node:
#                 return node
#             if model < node.car.model:
#                 node.left = delete(node.left, model)
#             elif model > node.car.model:
#                 node.right = delete(node.right, model)
#             else:
#                 if not node.left:
#                     return node.right
#                 if not node.right:
#                     return node.left
#                 temp = self._find_min(node.right)
#                 node.car = temp.car
#                 node.right = delete(node.right, temp.car.model)
#             return node
#
#         self.root = delete(self.root, model)
#         self._size -= 1
#
#     def search(self, model):
#         def find(node, model):
#             if not node:
#                 return None
#             if model == node.car.model:
#                 return node.car
#             elif model < node.car.model:
#                 return find(node.left, model)
#             else:
#                 return find(node.right, model)
#
#         return find(self.root, model)
#
#     def __len__(self):
#         return self._size
#
#     def sell_car(self, client, model):
#         car = self.search(model)
#         if car:
#             print(f"Автомобіль {car} продано клієнту {client}.")
#             self.remove(model)
#         else:
#             print(f"Автомобіль з маркою '{model}' не знайдено.")
#
#
# park = CarPark()
# park.add(Car("Toyota", "Camry", 2018))
# park.add(Car("BMW", "X5", 2020))
# park.add(Car("Audi", "A4", 2019))
#
# print("Кількість авто:", len(park))
# park.sell_car("Іван", "X5")
# print("Кількість авто після продажу:", len(park))




####
import random
import json

# Глобальні змінні для статистики
stats = {"wins": 0, "losses": 0}
filename = "game_stats.json"


def start_new_game():
    number = random.randint(1, 100)
    attempts = 0
    print("Комп'ютер загадав число від 1 до 100.")

    while True:
        try:
            guess = int(input("Введіть вашу відповідь: "))
        except ValueError:
            print("Будь ласка, введіть ціле число.")
            continue

        attempts += 1

        if guess < number:
            print("Більше.")
        elif guess > number:
            print("Менше.")
        else:
            print(f"Правильно! Ви вгадали число за {attempts} .")
            if attempts <= 4:
                print("Ви перемогли!")
                stats["wins"] += 1
            else:
                print("Комп'ютер переміг!")
                stats["losses"] += 1
            break


def show_result():
    print(f"Перемог: {stats['wins']}, Поразок: {stats['losses']}")


def save_data():
    try:
        with open(filename, 'w') as file:
            json.dump(stats, file)
        print("Дані збережено.")
    except Exception as e:
        print(f"Помилка збереження: {e}")


def load_data():
    global stats
    try:
        with open(filename, 'r') as file:
            stats = json.load(file)
        print("Дані завантажено.")
    except FileNotFoundError:
        print("Файл не знайдено. Починаємо з нуля.")
    except Exception as e:
        print(f"Помилка завантаження: {e}")


# Меню
def main():
    load_data()
    while True:
        print("\nМеню:")
        print("1. Почати нову гру")
        print("2. Вивести результат")
        print("3. Зберегти дані")
        print("4. Завантажити дані")
        print("5. Вийти")
        choice = input("Ваш вибір: ")

        if choice == '1':
            start_new_game()
        elif choice == '2':
            show_result()
        elif choice == '3':
            save_data()
        elif choice == '4':
            load_data()
        elif choice == '5':
            save_data()
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()

###
import json
import pickle

bands = {}

# Додати новий гурт
def add_band(name):
    if name not in bands:
        bands[name] = []
        print(f"Гурт '{name}' додано.")
    else:
        print(f"Гурт '{name}' вже існує.")

# Додати альбом до гурту
def add_album(band_name, album_name):
    if band_name in bands:
        bands[band_name].append(album_name)
        print(f"Альбом '{album_name}' додано до гурту '{band_name}'.")
    else:
        print(f"Гурту '{band_name}' не існує. Спочатку додайте гурт.")

# Зберегти в JSON
def save_json(filename='bands.json'):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(bands, f, ensure_ascii=False, indent=4)
        print("Дані збережено у форматі JSON.")
    except Exception as e:
        print(f"Помилка при збереженні JSON: {e}")

# Завантажити з JSON
def load_json(filename='bands.json'):
    global bands
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            bands = json.load(f)
        print("Дані завантажено з JSON.")
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Помилка при завантаженні JSON: {e}")

# Зберегти в pickle
def save_pickle(filename='bands.pkl'):
    try:
        with open(filename, 'wb') as f:
            pickle.dump(bands, f)
        print("Дані збережено у форматі pickle.")
    except Exception as e:
        print(f"Помилка при збереженні pickle: {e}")

# Завантажити з pickle
def load_pickle(filename='bands.pkl'):
    global bands
    try:
        with open(filename, 'rb') as f:
            bands = pickle.load(f)
        print("Дані завантажено з pickle.")
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Помилка при завантаженні pickle: {e}")

#меню
def main():
    while True:
        print("\nМеню:")
        print("1. Додати гурт")
        print("2. Додати альбом")
        print("3. Зберегти у JSON")
        print("4. Завантажити з JSON")
        print("5. Зберегти у Pickle")
        print("6. Завантажити з Pickle")
        print("7. Показати всі дані")
        print("8. Вийти")

        choice = input("Ваш вибір: ")

        if choice == '1':
            name = input("Назва гурту: ")
            add_band(name)
        elif choice == '2':
            band = input("Назва гурту: ")
            album = input("Назва альбому: ")
            add_album(band, album)
        elif choice == '3':
            save_json()
        elif choice == '4':
            load_json()
        elif choice == '5':
            save_pickle()
        elif choice == '6':
            load_pickle()
        elif choice == '7':
            for band, albums in bands.items():
                print(f"{band}: {', '.join(albums) if albums else 'без альбомів'}")
        elif choice == '8':
            print("До зустрічі!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()

###
import threading

numbers = []
input_done = threading.Event()

def input_numbers():
    print("Вводьте числа (порожній рядок для завершення):")
    while True:
        inp = input("Число: ")
        if inp == "":
            break
        try:
            num = float(inp)
            numbers.append(num)
        except ValueError:
            print("Будь ласка, введіть число.")
    input_done.set()  # Сигнал, що введення завершено

def calculate_sum():
    input_done.wait()
    total = sum(numbers)
    print(f"Сума чисел: {total}")

def calculate_average():
    input_done.wait()
    if numbers:
        avg = sum(numbers) / len(numbers)
        print(f"Середнє арифметичне: {avg}")
    else:
        print("Список порожній, неможливо обчислити середнє.")

# Створення потоків
input_thread = threading.Thread(target=input_numbers)
sum_thread = threading.Thread(target=calculate_sum)
avg_thread = threading.Thread(target=calculate_average)

# Запуск потоків
input_thread.start()
sum_thread.start()
avg_thread.start()

# Очікування завершення
input_thread.join()
sum_thread.join()
avg_thread.join()



###1
{
    "Київ": "Сонячно, 25°C",
    "Львів": "Дощ, 18°C",
    "Одеса": "Хмарно, 22°C"
}
import socket
import json

def load_weather_data():
    with open('weather_data.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def handle_client(client_socket):
    city = client_socket.recv(1024).decode('utf-8')
    weather_data = load_weather_data()
    forecast = weather_data.get(city, "Невідоме місто")
    client_socket.send(forecast.encode('utf-8'))
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))
    server.listen(5)
    print("Сервер запущено. Очікування підключень...")

    while True:
        client_socket, addr = server.accept()
        print(f"Підключено до {addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    main()
import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5555))
    city = input("Введіть назву міста: ")
    client.send(city.encode('utf-8'))
    forecast = client.recv(1024).decode('utf-8')
    print(f"Прогноз погоди: {forecast}")
    client.close()

if __name__ == "__main__":
    main()




#2
import socket

def handle_client(client1, client2):
    while True:
        try:
            message = client1.recv(1024).decode('utf-8')
            if not message:
                break
            client2.send(message.encode('utf-8'))
        except:
            break

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))
    server.listen(2)
    print("Сервер запущено. Очікування підключень...")

    client1, addr1 = server.accept()
    print(f"Підключено клієнта 1: {addr1}")
    client1.send("Ви підключені. Очікування другого клієнта...".encode('utf-8'))

    client2, addr2 = server.accept()
    print(f"Підключено клієнта 2: {addr2}")
    client2.send("Ви підключені. Починайте спілкування.".encode('utf-8'))
    client1.send("Другий клієнт підключився. Починайте спілкування.".encode('utf-8'))

    while True:
        handle_client(client1, client2)
        handle_client(client2, client1)

if __name__ == "__main__":
    main()
import socket
import threading

def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print("З'єднання з сервером втрачено.")
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5555))

    name = input("Введіть ваше ім'я: ")
    client.send(name.encode('utf-8'))

    threading.Thread(target=receive_messages, args=(client,)).start()

    while True:
        message = input()
        if message.lower() == 'вийти':
            break
        client.send(f"{name}: {message}".encode('utf-8'))

    client.close()

if __name__ == "__main__":
    main()


#3

import socket
import threading

def send_message(from_client, to_client):
    while True:
        try:
            message = from_client.recv(1024).decode('utf-8')
            if not message:
                break
            to_client.send(message.encode('utf-8'))
        except:
            break

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))
    server.listen(2)
    print("Сервер запущено. Очікування підключень...")

    client1, addr1 = server.accept()
    print(f"Підключено клієнта 1: {addr1}")
    client1.send("Ви підключені. Очікування другого клієнта...".encode('utf-8'))

    client2, addr2 = server.accept

