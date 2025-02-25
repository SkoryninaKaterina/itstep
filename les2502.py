# Завдання 1
# Створіть абстрактний клас Character, атрибути
#  name – ім’я
#  max_hp – максимальний рівень здоров’я
#  hp – нинішній рівень здоров’я
#  level – рівень персонажа(від 1 до 20)
#  intelligence – стат інтелекту
#  strength – стат сили
#  dexterity – стат спритності
#  mana – стат мани
#  defense – стат захисту
# Методи:
#  attack() – абстрактний метод
#  take_damage(damage) – отримує урон, зменшений на
# захист
#  level_up() – збільшує рівень
#  increase_stat(stat) – збільшує один з статів на 1
#  rest() – відпочинок(відновлює hp до максимального)
#  heal(heal_hp) – збільшує hp на heal_hp

class Character:
    def __init__(self, name, max_hp, level, intelligence, strength, dexterity, mana, defense):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.level = level
        self.intelligence = intelligence
        self.strength = strength
        self.dexterity = dexterity
        self.mana = mana
        self.defense = defense

    def attack(self):
        pass

    def take_damage(self,damage):
        if damage > self.defense:
            self.hp -= damage - self.defense

        if self.hp <= 0:
            self.hp = 0
            print(f'{self.name}You are dead')

    def level_up(self):
        if self.level < 20:
            self.level +=1


    def increase_stat(self, stat):
        if stat == 'intelligence':
            self.intelligence += 1
        elif stat == 'strength':
            self.strength += 1
        elif stat == 'dexterity':
            self.dexterity += 1
        elif stat == 'mana':
            self.mana += 1
        else:
                self.defense += 1

    def rest(self):
        self.hp = self.max_hp

    def heal(self, heal_hp):
        self.hp += heal_hp
        if self.hp > self.max_hp:
            self.hp = self.max_hp

# class Warrior(Character):
#     def __init__(self, name, max_hp, hp, level, intelligence, strength, dexterity, mana, defense):
#         super().__init__(name, max_hp, hp, level, intelligence, strength, dexterity, mana, defense)
#         self.strength += 2
#         self.defense += 1
#
#     def attack(self):
#         return self.strength * 2


# Створіть дочірній клас Paladin
# Методи:
#  attack() – наносить 4*strength урону та зменшує mana на
# 5, якщо недостатньо, то наносить strength урону
#  shield() – збільшує стат defense на 4+level
#  unshield() – зменшує стат defense на 4+level
#  heal_ally(ally) – лікує союзника на 5 + 2*level + 0.5*mana

class Paladin(Character):
    def attack(self):
        if self.mana >= 5:
            dem = self.strength * 4
            self.mana -= 5

        else:
            dem = self.strength
        return dem

    def shield(self):
        self.defense += 4 + self.level

    def unshield(self):
        self.defense -= 4 + self.level

    def heal_ally(self, ally):
        heal_hp = 5 + 2 * self.level + 0.5 * self.mana

        ally.heal(heal_hp)

paladin1 = Paladin('ivan', 100, 6, 5, 10, 10, 10, 10)
paladin2 = Paladin('petro', 100, 6, 5, 10, 10, 10, 10)

paladin2.take_damage(10)

print(paladin2.hp)

paladin1.heal_ally(paladin2)

print(paladin2.hp)



class Mage(Character):
    def fireball(self):
        if self.mana >=5:
            dem = 3 + 2 * self.intelligence
            self.mana -= 5
            return dem
        else:
            return 0

    def attack(self):
        if self.mana >=3:
            dem = 4 + 3 * self.intelligence
            self.mana -= 3
            return dem
        else:
            return 0

    def heal_ally(self, ally):
        heal_hp = 3 + self.level + 3 * self.intelligence
        ally.heal(heal_hp)




