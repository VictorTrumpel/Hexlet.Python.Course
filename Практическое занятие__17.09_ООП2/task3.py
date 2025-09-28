class Character:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Имя персонажа должно быть непустой строкой")
        self.name = name
        self.inventory = {}

    def addItem(self, item, qty=1):
        if not isinstance(item, str) or not item.strip():
            raise ValueError("Название предмета должно быть непустой строкой")
        if not isinstance(qty, int) or qty <= 0:
            raise ValueError("Количество должно быть положительным целым числом")
        if item in self.inventory:
            self.inventory[item] += qty
        else:
            self.inventory[item] = qty

    def __contains__(self, item):
        return item in self.inventory

    def __len__(self):
        return len(self.inventory)

    def __getitem__(self, item):
        if item not in self.inventory:
            raise KeyError(f"Предмет '{item}' отсутствует в инвентаре")
        return self.inventory[item]

    def __setitem__(self, item, qty):
        if not isinstance(qty, int) or qty < 0:
            raise ValueError("Количество должно быть целым неотрицательным числом")
        if qty == 0:
            self.inventory.pop(item, None)
        else:
            self.inventory[item] = qty

    def __str__(self):
        return f"Персонаж '{self.name}', предметов в инвентаре: {len(self)}"

    def __repr__(self):
        return f"Character(name={self.name!r}, inventory={self.inventory})"

hero = Character("Рыцарь")
hero.addItem("меч")
print("меч" in hero)   
print(len(hero))       
print(hero["меч"])     

hero["меч"] = 2
print(hero["меч"])     

hero.addItem("щит", 3)
print(len(hero))       
print(hero["щит"])     

try:
    print(hero["лук"])
except KeyError as e:
    print(e)          
