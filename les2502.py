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


