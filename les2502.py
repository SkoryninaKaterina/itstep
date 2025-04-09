class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class TreeNode:
    def __init__(self, car):
        self.car = car
        self.left = None
        self.right = None


class CarPark:
    def __init__(self):
        self.root = None
        self._size = 0

    def add(self, car):
        def insert(node, car):
            if not node:
                return TreeNode(car)
            if car.model < node.car.model:
                node.left = insert(node.left, car)
            else:
                node.right = insert(node.right, car)
            return node

        self.root = insert(self.root, car)
        self._size += 1

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def remove(self, model):
        def delete(node, model):
            if not node:
                return node
            if model < node.car.model:
                node.left = delete(node.left, model)
            elif model > node.car.model:
                node.right = delete(node.right, model)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                temp = self._find_min(node.right)
                node.car = temp.car
                node.right = delete(node.right, temp.car.model)
            return node

        self.root = delete(self.root, model)
        self._size -= 1

    def search(self, model):
        def find(node, model):
            if not node:
                return None
            if model == node.car.model:
                return node.car
            elif model < node.car.model:
                return find(node.left, model)
            else:
                return find(node.right, model)

        return find(self.root, model)

    def __len__(self):
        return self._size

    def sell_car(self, client, model):
        car = self.search(model)
        if car:
            print(f"Автомобіль {car} продано клієнту {client}.")
            self.remove(model)
        else:
            print(f"Автомобіль з маркою '{model}' не знайдено.")


park = CarPark()
park.add(Car("Toyota", "Camry", 2018))
park.add(Car("BMW", "X5", 2020))
park.add(Car("Audi", "A4", 2019))

print("Кількість авто:", len(park))
park.sell_car("Іван", "X5")
print("Кількість авто після продажу:", len(park))



