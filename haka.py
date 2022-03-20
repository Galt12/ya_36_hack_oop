from random import random

class Person():
    """Общие характеристики"""
    def __init__(
        self,
        name, 
        hp,
        ata,
        df,
    ) -> None:
        self.name = name
        self.hp = hp
        self.df = df
        self.ata = ata

    def get_attack(self,dmg):
        self.hp  -= - (dmg - self.df)

class Paladin(Person):
    def __init__(
        self,
        name,
        hp,
        df,
        ata
    ):
        super().__init__(name, hp, df, ata)
        self.hp = hp * 2 

class Warrior(Person):
    def __init__(
        self,
        name,
        hp,
        df,
        ata
    ):
        super().__init__(name, hp, df, ata)
        self.ata = 2 * ata

def list_name():
    pass

def create_person():
    """Создаем персонажей"""
    opp1 = Paladin('A', 100, 5, 10)
    opp2 = Warrior('B', 100, 4, 15)
    return opp1, opp2

def battle_arena(opp1, opp2):
    """Описание битвы"""
    attack_to = opp1.ata
    damage = attack_to - attack_to * opp2.get_attack()
    message = (f'{opp1.name} наносит удар по {opp2.name}')
    print(message)

def main():
    battle_arena()

if __name__ == '__main__':
    main()