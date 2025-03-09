# Завдання 1
# Використовуючи класи з практичної реалізуйте клас Shop з
# трьома чергами до кас. Кожна черга реалізується через
# двозв’язний список
# Атрибути
#  queue1, queue2, queue3 – черги до кас
# Методи
#  add_buyer(name, idx) – додає покупця в кінець черги
# номер idx
#  serve_buyer(idx) – обслуговує покупця з черги
# idx(вивести повідомлення та видалити покупця з черги)
# Якщо черга стала порожньою, то викликати _reorder(idx)
#  _reorder(idx) – з усіх черг останній покупець переходить
# в чергу з номером idx
#  display_info() – виводить на екран 3 черги
# Посилання на код
# # Приклад використання
# shop = Shop()
# shop.add_buyer("Олег", 1)
# Домашнє завдання
# shop.add_buyer("Марина", 2)
# shop.add_buyer("Марія", 2)
# shop.add_buyer("Андрій", 3)
# shop.add_buyer("Ірина", 1)
# shop.add_buyer("Василь", 2)
# shop.add_buyer("Тетяна", 3)
# shop.add_buyer("Сергій", 3)
# shop.add_buyer("Анна", 3)
# print("Черги:")
# shop. display_info()
# shop.serve_buyer(1)
# shop.serve_buyer(2)
# shop.serve_buyer(3)
# print("Після обслуговування покупців:")
# shop. display_info()
# shop.serve_buyer(1)
# print("Покупці перейшли до вільної каси:")
# shop. display_info()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.data} -> {self.next}"


class DoubleLinkedList:
    """
    Клас двозв'язного списку.
    """

    def __init__(self):
        """
        Ініціалізація порожнього списку.
        """
        self.head = None
        self.tail = None

    def __str__(self):
        return str(self.head)

    def push_end(self, data):
        """
        Додає елемент у кінець списку.
        :param data: Дані для додавання
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def push_start(self, data):
        """
        Додає елемент на початок списку.
        :param data: Дані для додавання
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop_end(self):
        """
        Видаляє останній елемент зі списку.
        :return: Дані видаленого елемента або None, якщо список порожній
        """
        if not self.tail:
            return None

        data = self.tail.data

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return data

    def pop_start(self):
        """
        Видаляє перший елемент зі списку.
        :return: Дані видаленого елемента або None, якщо список порожній
        """

        if not self.head:
            return None

        data = self.head.data

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data

    class Shop:
        def __init__(self):

            self.queue1 = DoubleLinkedList()
            self.queue2 = DoubleLinkedList()
            self.queue3 = DoubleLinkedList()

        def add_buyer(self, name, idx):

            if idx == 1:
                self.queue1.push_end(name)
            elif idx == 2:
                self.queue2.push_end(name)
            elif idx == 3:
                self.queue3.push_end(name)
            else:
                print("❌ Невірний номер каси!")

        def serve_buyer(self, idx):

            if idx == 1:
                buyer = self.queue1.pop_start()
                queue = self.queue1
            elif idx == 2:
                buyer = self.queue2.pop_start()
                queue = self.queue2
            elif idx == 3:
                buyer = self.queue3.pop_start()
                queue = self.queue3
            else:
                print("❌ Невірний номер каси!")
                return

            if buyer:
                print(f"✅ Покупець {buyer} був обслугований на касі {idx}.")
            else:
                print(f"⚠ Черга {idx} вже порожня.")


            if queue.head is None:
                self._reorder(idx)

        def _reorder(self, idx):

            last_buyer = None

            if self.queue3.tail:
                last_buyer = self.queue3.pop_end()
            elif self.queue2.tail:
                last_buyer = self.queue2.pop_end()
            elif self.queue1.tail:
                last_buyer = self.queue1.pop_end()

            if last_buyer:
                if idx == 1:
                    self.queue1.push_end(last_buyer)
                elif idx == 2:
                    self.queue2.push_end(last_buyer)
                elif idx == 3:
                    self.queue3.push_end(last_buyer)
                print(f"🔄 Покупець {last_buyer} переміщений у чергу {idx}.")
            else:
                print("⚠ Немає покупців для переміщення.")

        def display_info(self):

            print("🛒 Черга 1:", self._queue_to_list(self.queue1))
            print("🛒 Черга 2:", self._queue_to_list(self.queue2))
            print("🛒 Черга 3:", self._queue_to_list(self.queue3))

        def _queue_to_list(self, queue):

            current = queue.head
            result = []
            while current:
                result.append(current.data)
                current = current.next
            return result


    shop = Shop()
    shop.add_buyer("Олег", 1)
    shop.add_buyer("Марина", 2)
    shop.add_buyer("Марія", 2)
    shop.add_buyer("Андрій", 3)
    shop.add_buyer("Ірина", 1)
    shop.add_buyer("Василь", 2)
    shop.add_buyer("Тетяна", 3)
    shop.add_buyer("Сергій", 3)
    shop.add_buyer("Анна", 3)

    print("\n Черги перед обслуговуванням:")
    shop.display_info()

    shop.serve_buyer(1)
    shop.serve_buyer(2)
    shop.serve_buyer(3)

    print("\n Після обслуговування покупців:")
    shop.display_info()

    shop.serve_buyer(1)

    print("\n Покупці перейшли до вільної каси:")
    shop.display_info()
