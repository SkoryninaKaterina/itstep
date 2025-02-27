# Завдання 1
# Створіть клас Recipe з атрибутами
#  name – назва страви
#  ingredients – список продуктів
#  text – текст рецепту
#  time – час приготування
# методи:
#  __str__(self) – повертає назву страви
#  __contains__(self, item) – перевіряє чи є інгредієнт в
# рецепті
#  __gt__(self, other) – перевіряє чи є час приготування self
# більшим за other
#  display_info(self) – виводить всю інформацію про рецепт
# Створіть декілька рецептів та добавте їх у список.
# Виведіть назви тих рецептів, які містять інгредієнт томат
# Виведіть повну інформацію рецепта з найменшим часом
# приготування, скористайтесь функцією min
# Приклад рецептів:
# Recipe("Піца",
# Домашнє завдання
#  ["борошно", "вода", "дріжджі", "томат", "сир"],
#  "Готуємо тісто, додаємо інгредієнти та запікаємо",
#  30)
#
#  Recipe("Салат",
#  ["томат", "огірок", "зелень", "олія"],
#  "Нарізаємо овочі, додаємо зелень та поливаємо
# олією",
#  10)
#
#  Recipe("Суп",
#  ["вода", "картопля", "морква", "м'ясо"],
#  "Варимо всі інгредієнти до готовності",
#  45)


class Recipe:
    def __init__(self, name, ingredients, text, time):
        self.name = name
        self.ingredients = ingredients
        self.text = text
        self.time = time

    def __str__(self):
        return self.name

    def __contains__(self, item):
        return item in self.ingredients

    def __gt__(self, other):
        return self.time > other.time

    def __lt__(self, other):
        return self.time < other.time

    def __repr__(self):
        return f"Recipe({self.name}, {self.ingredients}, {self.text}, {self.time})"

    def display_info(self):
        print(f"🔹 Назва: {self.name}\n🛒 Інгредієнти: {', '.join(self.ingredients)}\n📜 Рецепт: {self.text}\n⏳ Час: {self.time} хвилин\n")


# Створюємо рецепти
recipes = [
    Recipe("Піца", ["борошно", "вода", "дріжджі", "томат", "сир"], "Готуємо тісто, додаємо інгредієнти та запікаємо", 30),
    Recipe("Салат", ["томат", "огірок", "зелень", "олія"], "Нарізаємо овочі, додаємо зелень та поливаємо олією", 10),
    Recipe("Суп", ["вода", "картопля", "морква", "м'ясо"], "Варимо всі інгредієнти до готовності", 45)
]

# Вивести рецепти, що містять "томат"
print("🍅 Рецепти, які містять томат:")
for recipe in recipes:
    if "томат" in recipe:
        print(f"- {recipe}")

# Знайти рецепт із найменшим часом приготування
fastest_recipe = min(recipes)
print("\n⏳ Рецепт із найменшим часом приготування:")
fastest_recipe.display_info()







