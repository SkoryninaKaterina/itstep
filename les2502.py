# наслідування

# class Parent:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         print(f"клас Parent")
#         print(f'{self.name}, {self.age} років')
#
# # наслідування
#
# class Child(Parent):
#     def play(self):   # новий метод
#         print('клас Child')
#         print(f'{self.name} грається')
# # переведення числа в діапазон [0, 100]
#
#     def show_info(self):  # перевизначений метод
#         print(f"клас Child")
#         print(f'{self.name}, {self.age} років')
# value = -10
#
# # варіант через if
# # if value > 100:
# #     value = 100
# # elif value < 0:
# #     value = 0
#
# class Daughter(Parent):
#     def __init__(self, name, age, dream):
#         self.name = name
#         self.age = age
#         self.dream = dream
# # через min max
#
# value = -10
# new_value = min(value, 100)
# new_value = max(new_value, 0)
#
# # mother = Parent('Marry', 36)
# # mother.show_info()
# #
# # print()
# #
# # child = Child('Rony', 8)
# # child.show_info()
# # child.play()
# new_value = max(0, min(100, value))  # clip
#
# # daughter = Daughter("Linda", 10, 'became a doctor')
# # daughter.show_info()
#
# # код з класом Parent
# mother = Parent('Marry', 36)
# mother.show_info()
# print(new_value)
#
# # використання методів батьківського класу
# from abc import ABC, abstractmethod
#
# class Animal(ABC):  # абстрактний клас(не можна створити об'єкт)
#     @abstractmethod
#     def __init__(self, name, age):
#         self._check_name(name)
#         self._check_age(age)
#         self.name = name
#         self.age = age
#
# # класи для Транспортні засоби
#     def _check_name(self, name):
#         # перевірка чи тип даних str
#         if not isinstance(name, str):
#             raise ValueError(f"Ім'я має бути рядком, отримано тип {type(name)}")
#
# class Vehicle:
#     def __init__(self, owner,  # власник
#                  max_fuel_level,  # максимальний рівень пального
#                  milliage  # км / 1 літр пального
#                  ):
#         self.owner = owner
#         self.max_fuel_level = max_fuel_level
#         self.fuel_level = max_fuel_level # бак повний
#         self.milliage = milliage
#         # лише літери та символи ' ' '-'
#         for sym in name:
#             if not(sym.isalpha() or sym in ' -'):
#                 raise ValueError("Ім'я має складатися лише з літер та ' -'")
#
#     def move(self, speed, distance):
#         need_fuel = distance / self.milliage
#     def _check_age(self, age):
#         # перевірка чи тип даних int float
#         if not isinstance(age, (int, float)):
#             raise ValueError(f"Вік має бути числом, отримано тип {type(age)}")
#
#         if self.fuel_level < need_fuel: # не хватає пального
#             print('не хватає пального')
#         else:
#             self.fuel_level -= need_fuel
#             time = distance / speed
#         if age <= 0 or age >= 20:
#             raise ValueError(f"Вік має бути в діапазоні [0, 20]")
#
#             print(f"Проїхали {distance}км за {time}год")
#
#     def info(self):
#         print(f"Ім'я: {self.name}, {self.age} років")
#
#     def add_fuel(self, fuel):
#         self.fuel_level += fuel
#
# class Car(Vehicle):
#     pass
# class Cat(Animal): # name, age, is_vaccinated
#     def __init__(self, name, age, is_vaccinated=True):
#         super().__init__(name, age)
#         self.is_vaccinated = is_vaccinated
#
#     def catch_mouse(self):
#         print("Ловить мишу")
#
# class Bicycle(Vehicle):
#     def __init__(self, owner, max_fuel_level, milliage):
#         self.owner = owner
#         self.max_fuel_level = max_fuel_level
#         self.fuel_level = max_fuel_level  # бак повний
#         self.milliage = milliage
#     def info(self):  # додатково писало що це кіт
#         print("Кіт")
#         # super() # super -- батьківський клас
#         super().info() # info з класу Animal
#
#         self.used_motor = False # мотор виключений
#         if self.is_vaccinated:
#             print("Вакцинований")
#         else:
#             print("Потрібно вакцинувати")
#
#
#     def move(self, speed, distance):  # теж рухається але не трабе пального
#         if not self.used_motor:
#             time = distance / speed
#             print("Без пального")
#             print(f"Проїхали {distance}км за {time}год")
#             return
# # cat1 = Cat('Tom', 5)
# # cat1.info()
# # #cat1.catch_mouse()
# # print()
# #
# # cat = Animal('Roger', 10)
# # cat.info()
#
#         # мотор вклюсений(код з Vehicle.move)
# # приховані атрибути\методи
#
#         need_fuel = distance / self.milliage
# class Cat(Animal): # name, age, is_vaccinated
#     def __init__(self, name, age, is_vaccinated=True):
#         super().__init__(name, age)
#         self._is_vaccinated = is_vaccinated  # прихований атрибут
#
#         if self.fuel_level < need_fuel:  # не хватає пального
#             print('не хватає пального')
#         else:
#             self.fuel_level -= need_fuel
#             time = distance / speed
#     def catch_mouse(self):
#         print("Ловить мишу")
#
#             print("З пальним")
#             print(f"Проїхали {distance}км за {time}год")
#     def info(self):  # додатково писало що це кіт
#         print("Кіт")
#         # super() # super -- батьківський клас
#         super().info() # info з класу Animal
#
#     def turn_on(self):
#         self.used_motor = True
#         if self._is_vaccinated:
#             print("Вакцинований")
#         else:
#             print("Потрібно вакцинувати")
#
#     def vaccinate(self):
#         self._is_vaccinated = True
#
#     def turn_off(self):
#         self.used_motor = False
#     def unvaccinate(self):
#         self._is_vaccinated = False
#
#
# class Plane(Vehicle):
# class Kitten(Cat):
#     pass
#
#
# cat1 = Cat('Tom', 2.5)
#
# cat1.info()
#
# bike = Bicycle('John', 100, 50)
# bike.move(20, # швидкість
#          15  # кілометри
#          )
# cat1.unvaccinate()
#
# bike.turn_on()
# cat1.info()
#
# bike.move(40,
#           100)
# # print(cat1._Cat__is_vaccinated)
#
# kitten = Kitten("Murchyck", 1)
# kitten.info()

# Завдання 1
# Створіть абстрактний клас Robot з атрибутами:
#  name – назва робота або id
#  battery_level – рівень заряду(за замовчуванням 100%)
#  status – поточний стан (один з on, off, working)
# Методи:
#  info() – виводить інформацію
#  charge() – відновлює заряд до 100%
#  turn_on() – змінює стан на on
#  turn_off() – змінює стан на off


from abc import ABC, abstractmethod
from random import choice


class Robot(ABC):
    def __init__(self, name, battery_level=100, status='off'):
        self.name = name
        self.battery_level = battery_level
        self.status = status

    @abstractmethod
    def info(self):
        print(f"Назваобота або ID: {self.name}")
        print(f"Рівень заряду: {self.battery_level}")
        print(f"Статус: {self.status}")


    def charge(self):
        self.battery_level = 100


    def turn_on(self):
        self.status = 'on'


    def turn_off(self):
        self.status = 'off'


# robot1 = Robot('abc', 90)
# robot1.info()

# Завдання 2
# Створіть дочірній клас CleaningRobot
# Додаткові атрибути:
#  dust_capacity – ємність контейнеру для пилу(за
# замовчуванням 0%)
#  water_capacity – ємність контейнеру для води(за
# замовчуванням 100%)
#  cleaning_mode – тип прибирання(вологе або сухе)
# Методи:
#  info() – додатково виводить інформацію про робота
# Практичне завдання
#  turn_on() – якщо контейнер для пилу повний або
# контейнер для води порожній то виводить повідомлення,
# інакше запускається turn_on() з класу Robot
#  empty_dustbin() – очищає контейнер для пилу
#  fill_water() – заповнює контейнер для води
#  swap_mode() – змінює тип прибирання на протилежний
#  clean(energy, dust, water=None) – чистить поверхню,
# якщо прибирання сухе, то просто перенести пил у
# контейнер(якщо місця не достатньо вивести помилку),
# якщо прибирання вологе то додатково витратити воду.
# Також зменшує рівень заряду на energy

#
# class CleaningRobot(Robot):
#     def __init__(self, name,battery_level=100, status='off', dust_capacity=0, water_capacity=100, cleaning_mode='dry'):
#         super().__init__(name, battery_level, status)
#         self.dust_capacity = dust_capacity
#         self.water_capacity = water_capacity
#         self.cleaning_mode = cleaning_mode
#
#     def info(self):
#         super().info()
#         print(f"Ємність контейнеру для пилу: {self.dust_capacity}")
#         print(f"Рівень заряду батареї: {self.battery_level}")
#         print(f"Тип прибирання: {self.cleaning_mode}")
#         print(f"Ємність контейнеру для води: {self.water_capacity}")
#
#     def turn_on(self):
#         if self.dust_capacity == 100 or self.water_capacity == 0:
#             print("Контейнер для пилу повний або контейнер для води порожній")
#         else:
#             super().turn_on()
#
#     def empty_dustbin(self):
#         self.dust_capacity = 0
#
#     def fill_water(self):
#         self.water_capacity = 100
#
#     def swap_mode(self):
#         if self.cleaning_mode == 'wet':
#             self.cleaning_mode = 'dry'
#         else:
#             self.cleaning_mode = 'wet'
#
#     def clean(self, energy, dust, water=None):
#         if self.status == 'off':
#             print('Robot is off')
#             return
#
#         if self.battery_level < energy:
#             print("Недостатньо заряду")
#
#
#
#
#         if self.dust_capacity + dust > 100:
#             print("Контейнер для пилу повний")
#             return
#
#
#         if self.cleaning_mode == 'wet':
#             if water is None:
#                 print("Води не вистачить")
#                 return
#             if self.water_capacity < water:
#                 print("Води не вистачить")
#                 return
#
#
#             self.water_capacity -= water
#             self.dust_capacity += dust
#             self.battery_level -= energy
#
#             if self.cleaning_mode == 'wet':
#                 self.water_capacity -= water
#
# robot2 = CleaningRobot('abc', 90)
# robot2.turn_on()
# robot2.clean(10, 20, 50)
# robot2.info()

# Завдання 4
# Створіть дочірній клас AssistantRobot
# Додаткові атрибути:
#  tasks – список завдань(за замовчуванням порожній)
#  current_task – поточне завдання(за замовчуванням None)
# Методи:
#  info() – додатково виводить інформацію про робота
#  add_task(task) – додає завдання до списку
#  change_task() – змінює поточне завдання, виводить на
# екран список завдань та просить користувача вибрати
# одне з них
#  execute_task() – виконує поточне завдання, видяляє його
# зі списку, та змінює current_task на наступне


class AssistantRobot(Robot):
    def __init__(self, name, battery_level=100, status='off', tasks=None, current_task=None):
        super().__init__(name, battery_level, status)
        if tasks is None:
            tasks = []
        else:
            self.tasks = tasks
        self.current_task = current_task

    def info(self):
        super().info()
        for task in self.tasks:
            print(task)
        print(f"Поточне завдання: {self.current_task}")

    def add_task(self, task):
        self.tasks.append(task)

    def change_task(self):
        if not self.tasks:
            print("Список завдань порожній")
            return

        print("Список завдань: ")
        for ind, task  in enumerate(self.tasks, start=1):
            print(f"{ind}. {task}")

        choise = int(input("Виберіть завдання: "))
        self.current_task = self.tasks[choise - 1]
        self.tasks.pop(choise - 1)

    def execute_task(self):
        if not self.current_task:
            print("Немає поточного завдання")
            return

        print(f"Виконуємо завдання: {self.current_task}")
        self.tasks.remove(self.current_task)

        if self.tasks:
            self.current_task = self.tasks[0]
        else:
            print('Завдань немає')
            self.current_task = None