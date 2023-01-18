
class Hero:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def __str__(self):
        return f'Name of hero - {self.name}\n'\
              f'Ability - {self.ability}'

class Hero_super(Hero):

    def __init__(self, name, ability):
        super().__init__(name, ability)

    def __str__(self):
        return f'{self.name} {self.ability}'

    def itis(self):
        return f'{self.name} - it is super_hero'

s1 = Hero('Doctor Strange', 'can create complex shields and barriers')
s = Hero_super('Spiderman','can fly using spy web')

print(f'Маг метод str: {s}')
print(f'Метод который выводит имя героя и надпись it is super_hero: {s.itis()}')
