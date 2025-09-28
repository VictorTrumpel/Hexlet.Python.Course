class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def __eq__(self, other):
        if not isinstance(other, Animal):
            return False
        return (self.name, self.species, self.age) == (other.name, other.species, other.age)

    def __repr__(self):
        return f"{self.species} '{self.name}', {self.age} года(лет)"


class AnimalNode(Animal):
    def __init__(self, name, species, age, parent=None):
        super().__init__(name, species, age)
        self.parent = None
        self.children = []

        if parent is not None:
            self.set_parent(parent)

    def set_parent(self, parent):
        self.parent = parent
        if self not in parent.children:
            parent.children.append(self)

    def __len__(self):
        total = len(self.children)
        for child in self.children:
            total += len(child)
        return total

    def __getitem__(self, index):
        return self.children[index]

    def __contains__(self, obj):
        for child in self.children:
            if child == obj or obj in child:
                return True
        return False

    def traverse(self):
        yield self
        for child in self.children:
            yield from child.traverse()

    def __repr__(self):
        return f"{self.species} '{self.name}', {self.age} года(лет), детей: {len(self.children)}"


# Пример использования
mama = AnimalNode("Луна", "Кошка", 4)
pup1 = AnimalNode("Мурзик", "Кот", 1, parent=mama)
pup2 = AnimalNode("Снежок", "Кот", 2, parent=mama)
pup3 = AnimalNode("Пушинка", "Кошка", 0, parent=pup1)

print("Мама:", mama)
print("Дети мамы:", mama.children)
print("Общее количество потомков у мамы:", len(mama))
print("Является ли Мурзик потомком Луны?", pup1 in mama)
print("Является ли Пушинка потомком Луны?", pup3 in mama)
print("Первый ребёнок Луны:", mama[0])

# Обход дерева
print("\nОбход дерева от мамы:")
for animal in mama.traverse():
    print(animal)
