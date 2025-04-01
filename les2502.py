#Завдання 1
# import time
# from collections import deque
#
#
# class FastFoodQueue:
#     def __init__(self):
#         self.queues = [deque() for _ in range(4)]  # 4 каси
#         self.order_queue = deque()  # Черга на отримання замовлення
#         self.service_duration_history = []  # Історія часу обслуговування
#
#     def add(self, client):
#         #Додає клієнта в найменшу чергу
#         shortest_queue = min(self.queues, key=len)
#         shortest_queue.append(client)
#         print(f"{client} став у чергу {self.queues.index(shortest_queue) + 1}")
#
#     def serve(self, idx):
#         #Обслуговує клієнта з обраної черги та додає його до черги отримання замовлення
#         if self.queues[idx]:
#             client = self.queues[idx].popleft()
#             order_time = time.time()
#             self.order_queue.append((client, order_time))
#             print(f"{client} зробив замовлення на касі {idx + 1}")
#         else:
#             print(f"Черга {idx + 1} порожня!")
#
#     def make_order(self):
#         #Видає готове замовлення клієнту та рахує час очікування
#         if self.order_queue:
#             client, order_time = self.order_queue.popleft()
#             wait_time = time.time() - order_time
#             self.service_duration_history.append(wait_time)
#             print(f"{client} отримав замовлення, чекав {wait_time:.2f} секунд")
#         else:
#             print("Немає замовлень для видачі!")
#
#     def show_statistics(self):
#         # Виводить мінімальний, максимальний і середній час обслуговування
#         if self.service_duration_history:
#             min_time = min(self.service_duration_history)
#             max_time = max(self.service_duration_history)
#             avg_time = sum(self.service_duration_history) / len(self.service_duration_history)
#             print(f"Статистика обслуговування: Мін: {min_time:.2f}, Макс: {max_time:.2f}, Середнє: {avg_time:.2f}")
#         else:
#             print("Немає даних для статистики!")
#
#
# if __name__ == "__main__":
#     fast_food = FastFoodQueue()
#     fast_food.add("Олег")
#     fast_food.add("Анна")
#     fast_food.add("Марія")
#     fast_food.add("Сергій")
#
#     fast_food.serve(0)
#     fast_food.serve(1)
#
#     time.sleep(2)
#     fast_food.make_order()
#     time.sleep(3)
#     fast_food.make_order()
#
#     fast_food.show_statistics()



# #завдання 2
#
# import heapq
#
#
# class Passenger:
#     def __init__(self, name, priority):
#         self.name = name
#         self.priority = priority
#
#     def __lt__(self, other):
#         return self.priority < other.priority
#
#
# class Zone:
#     def __init__(self, name):
#         self.name = name
#         self.passengers = []  # Використовуємо пріоритетну чергу
#
#     def add(self, passenger):
#         heapq.heappush(self.passengers, passenger)
#         print(f"{passenger.name} доданий до зони {self.name}")
#
#     def serve_passenger(self):
#         if self.passengers:
#             return heapq.heappop(self.passengers)
#         else:
#             print(f"Черга в зоні {self.name} порожня!")
#             return None
#
#
# class Airport:
#     def __init__(self):
#         self.zones = {
#             "Реєстрація": Zone("Реєстрація"),
#             "Контроль безпеки": Zone("Контроль безпеки"),
#             "Посадка": Zone("Посадка")
#         }
#         self.passengers = []  # Пасажири, які успішно пройшли всі етапи
#
#     def add(self, passenger):
#         self.zones["Реєстрація"].add(passenger)
#
#     def serve_registration(self):
#         passenger = self.zones["Реєстрація"].serve_passenger()
#         if passenger:
#             self.zones["Контроль безпеки"].add(passenger)
#
#     def serve_security_control(self):
#         passenger = self.zones["Контроль безпеки"].serve_passenger()
#         if passenger:
#             self.zones["Посадка"].add(passenger)
#
#     def serve_boarding(self):
#         passenger = self.zones["Посадка"].serve_passenger()
#         if passenger:
#             self.passengers.append(passenger)
#             print(f"{passenger.name} успішно пройшов всі етапи!")
#
#     def show_statistics(self):
#         print("Статистика аеропорту:")
#         for name, zone in self.zones.items():
#             print(f"{name}: {len(zone.passengers)} пасажирів у черзі")
#         print(f"Успішно пройшли всі етапи: {len(self.passengers)} пасажирів")
#
#
# # Тестування
# if __name__ == "__main__":
#     airport = Airport()
#     passengers = [
#         Passenger("Олег", 3),
#         Passenger("Анна", 1),
#         Passenger("Марія", 4),
#         Passenger("Сергій", 2)
#     ]
#
#     for p in passengers:
#         airport.add(p)
#
#     airport.serve_registration()
#     airport.serve_registration()
#     airport.serve_security_control()
#     airport.serve_boarding()
#
#     airport.show_statistics()



#завдання 3

import heapq


class Passenger:
    def __init__(self, name, priority, baggage=None):
        self.name = name
        self.priority = priority
        self.baggage = baggage if baggage else []

    def __lt__(self, other):
        return self.priority < other.priority


class Zone:
    def __init__(self, name):
        self.name = name
        self.passengers = []  # Використовуємо пріоритетну чергу

    def add(self, passenger):
        heapq.heappush(self.passengers, passenger)
        print(f"{passenger.name} доданий до зони {self.name}")

    def serve_passenger(self):
        if self.passengers:
            return heapq.heappop(self.passengers), True
        else:
            print(f"Черга в зоні {self.name} порожня!")
            return None, False


class RegistrationZone(Zone):
    def __init__(self):
        super().__init__("Реєстрація")

    def serve_passenger(self):
        if self.passengers:
            passenger = heapq.heappop(self.passengers)
            if "ticket" in passenger.baggage:
                return passenger, True
            else:
                print(f"{passenger.name} не може пройти реєстрацію – немає білету!")
                return passenger, False
        return None, False


class SecurityZone(Zone):
    def __init__(self):
        super().__init__("Контроль безпеки")

    def serve_passenger(self):
        if self.passengers:
            passenger = heapq.heappop(self.passengers)
            dangerous_items = {"knife", "gun", "explosives"}
            if any(item in dangerous_items for item in passenger.baggage):
                print(f"{passenger.name} не пройшов контроль безпеки – заборонені предмети в багажі!")
                return passenger, False
            return passenger, True
        return None, False


class BoardingZone(Zone):
    def __init__(self):
        super().__init__("Посадка")

    def serve_passenger(self):
        return super().serve_passenger()


class Airport:
    def __init__(self):
        self.zones = {
            "Реєстрація": RegistrationZone(),
            "Контроль безпеки": SecurityZone(),
            "Посадка": BoardingZone()
        }
        self.passengers = []  # Пасажири, які успішно пройшли всі етапи

    def add(self, passenger):
        self.zones["Реєстрація"].add(passenger)

    def serve_registration(self):
        passenger, success = self.zones["Реєстрація"].serve_passenger()
        if success:
            self.zones["Контроль безпеки"].add(passenger)

    def serve_security_control(self):
        passenger, success = self.zones["Контроль безпеки"].serve_passenger()
        if success:
            self.zones["Посадка"].add(passenger)

    def serve_boarding(self):
        passenger, success = self.zones["Посадка"].serve_passenger()
        if success:
            self.passengers.append(passenger)
            print(f"{passenger.name} успішно пройшов всі етапи!")

    def show_statistics(self):
        print("Статистика аеропорту:")
        for name, zone in self.zones.items():
            print(f"{name}: {len(zone.passengers)} пасажирів у черзі")
        print(f"Успішно пройшли всі етапи: {len(self.passengers)} пасажирів")


# Тестування
if __name__ == "__main__":
    airport = Airport()
    passengers = [
        Passenger("Олег", 3, ["ticket", "phone"]),
        Passenger("Анна", 1, ["ticket", "laptop"]),
        Passenger("Марія", 4, ["ticket"]),
        Passenger("Сергій", 2, ["ticket", "knife"])
    ]

    for p in passengers:
        airport.add(p)

    airport.serve_registration()
    airport.serve_registration()
    airport.serve_security_control()
    airport.serve_boarding()

    airport.show_statistics()



