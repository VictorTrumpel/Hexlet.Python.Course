class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def check_stock(self):
        if self.quantity > 0:
            return f'Продукт {self.name} в наличии. {self.quantity} шт.'
        else:
            return f'Продукт {self.name} закончился'

    def calculate_value(self):
        total = self.price * self.quantity
        return round(total, 1)



p1 = Product("Яблоко", 100, 50)
print(p1.check_stock())
print(p1.calculate_value())

p2 = Product('Хлеб', 75, 0)
print(p2.check_stock())
print(p2.calculate_value())