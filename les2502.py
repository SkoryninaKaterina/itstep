# Завдання 1
# Створіть клас однозв’язного списку SinglyLinkedList
# Методи
#  print() – виводить список на екран
#  push_end(data) – добавити в кінець
#  push_start(data) – добавити на початку
#  pop_start() – видалити перший елемент


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data} -> {self.next}'

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        return f'{self.head}'

    def push_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

#  push_start(data) – добавити на початку
    def push_start(self, data):
        new_node =Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head = new_node


data = SinglyLinkedList()

data.push_end(1)
print(data)
data.push_end(2)
print(data)
data.push_end(3)
print(data)
data.push_start(5)
print(data)
data.push_start(10)
print(data)