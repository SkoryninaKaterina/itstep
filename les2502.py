# Завдання 1
# Створіть клас Pet з атрибутами
#  name – ім’я тварини
#  satiety – рівень ситості(від 0 до 100, за замовчуванням 50)
#  energy – рівень енергії (від 0 до 100, за замовчуванням 50)
# Методи:
#  sleep() – збільшує energy до 100
#  eat(food_amont) – їсть, збільшує satiety на food_amount
#  play(activity_level) – абстрактний метод
#  make_sound() – просто pass
# Створіть клас Cat
# Методи:
#  play(activity_level) – якщо satiety > 60, зменшує energy на
# 2*acticity_level та satiety на acticity_level
#  make_sound() – виводить ‘Мяу’
#  catch_mouse() – якщо energy > 30, ловить мишу. Якщо
# satiety > 40, то грається з мишею, інакше їсть
# Створіть клас Dog
# Методи:
#  play(activity_level) – якщо satiety > 15, зменшує energy на
# Домашнє завдання
# acticity_level//2 та satiety на acticity_level//2
#  make_sound() – виводить ‘Гав’
#  fetch_ball() – ловить м’яча якщо satiety>10, зменшує
# energy на 5

class Pet:
    def __init__(self, name, satiety=50, energy=50):
        self.name = name
        self.satiety = satiety
        self.energy = energy

    def sleep(self):
        """Сон відновлює енергію до 100."""
        self.energy = 100

    def eat(self, food_amount):
        """Їжа збільшує ситість, але не більше 100."""
        self.satiety = min(self.satiety + food_amount, 100)

    def play(self, activity_level):
        pass

    def make_sound(self):
        pass

    def __str__(self):
        return f"{self.name} | Ситість: {self.satiety}, Енергія: {self.energy}"


class Cat(Pet):
    def play(self, activity_level):
        if self.satiety > 60:
            self.energy = max(self.energy - 2 * activity_level, 0)
            self.satiety = max(self.satiety - activity_level, 0)

    def make_sound(self):
        print('Мяу')

    def catch_mouse(self):
        if self.energy > 30:
            if self.satiety > 40:
                print(f"{self.name} грається з мишею.")









