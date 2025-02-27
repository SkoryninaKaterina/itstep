#завдання 1
# створіть клас Pasenger з атрибутами
# name - імя
# destination - місце куди прямує
#
class Passenger:
    def __init__(self, name, destination):
        self.name = name
        self.destination = destination

    def change_destination(self, new_destination):
        self.destination = new_destination

    def __str__(self):
        return f"Пасажир: {self.name}, Пункт призначення: {self.destination}"


passenger1 = Passenger("Олексій", "Київ")
print(passenger1)  # Пасажир: Олексій, Пункт призначення: Київ

passenger1.change_destination("Львів")
print(passenger1)  # Пасажир: Олексій, Пункт призначення: Львів


# Завдання 2
# Створіть клас Transport з атрибутами
# speed - швидкість
# методи
# move( destination, distanse) - рухається до місця призначення,
# виводить інформацію як довго їхали

class Transport:
    def __init__(self, speed):
        if speed <= 0:
            raise ValueError("Швидкість повинна бути більше 0")
        self.speed = speed

    def move(self, destination, distance):
        time = round(distance / self.speed )
        print(f"Транспорт рухається до {destination} протягом {time} годин")

    def __str__(self):
        return f"Швидкість: {self.speed} км/год."

car = Transport(60)

car.move("Київ", 100)
car.move("Львів", 500)
car.move("Одеса", 450)


# Завдання 3
# Створіть клас Bus з атрибутами
#  passengers – список пасажирів(об’єкти класу Passenger)
#  capacity – максимальна можлива кількість пасажирів
# Методи
#  board_passenger(passenger) – якщо є місце, додає
# пасажира
#  move(destination, distance) – висаджує всіх пасажирів, які
# хочуть вийти в даному місці(виводить їхню загальну
# кількість) та викликає батьківський метод move()

class Bus(Transport):
    def __init__(self, speed, capacity, passengers=None):
        super().__init__(speed)
        self.capacity = capacity
        self.passengers = passengers if passengers else []

    def board_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            print(f"{passenger.name} сів у автобус до {passenger.destination}.")
        else:
            print("Автобус повний, місць більше немає!")

    def move(self, destination, distance):

        leaving_passengers = [p for p in self.passengers
                              if p.destination == destination]
        self.passengers = [p for p in self.passengers
                           if p.destination != destination]

        print(f"🛑 Автобус прибув у {destination}. "
              f"Вийшло {len(leaving_passengers)} пасажирів.")

        super().move(destination, distance)

    def __str__(self):
        return (f"Автобус: {len(self.passengers)}/{self.capacity}"
                f" пасажирів, швидкість {self.speed} км/год.")


bus = Bus(speed=50, capacity=3)

passenger1 = Passenger("Олексій", "Київ")
passenger2 = Passenger("Марія", "Львів")
passenger3 = Passenger("Іван", "Київ")
passenger4 = Passenger("Анна", "Одеса")

bus.board_passenger(passenger1)
bus.board_passenger(passenger2)
bus.board_passenger(passenger3)
bus.board_passenger(passenger4)  # Автобус повний

print(bus)

bus.move("Київ", 100)  # Вийшли Олексій та Іван
print(bus)

bus.move("Львів", 500)  # Вийшла Марія
print(bus)
