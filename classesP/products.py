# 1. Базовый класс Product и производные классы для различных типов товаров
class Product:
    """
    Базовый класс, представляющий товар.
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price
#
    def get_details(self):
        return f"Товар: {self.name}, Цена: {self.price} руб."
#
class Electronics(Product):
    """
    Класс, представляющий электронный товар, наследующий класс Product.
    """
    def __init__(self, name, price, brand, warranty_period):
        super().__init__(name, price)
        self.brand = brand
        self.warranty_period = warranty_period
#
    def get_details(self):
        return f"Электроника: {self.name}, Бренд: {self.brand}, Цена: {self.price} руб, Гарантия: {self.warranty_period} лет"
#
class Clothing(Product):
    """
    Класс, представляющий одежду, наследующий класс Product.
    """
    def __init__(self, name, price, size, material):
        super().__init__(name, price)
        self.size = size
        self.material = material
#
    def get_details(self):
        return f"Одежда: {self.name}, Размер: {self.size}, Материал: {self.material}, Цена: {self.price} руб."
# добавляем класс HouseHoldChemicals - товары бытовой химии
class HouseHoldChemicals(Product):
    """
    Класс, представляющий товары бытовой химии, наследующий класс Product.
    """
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = volume # объем в мл
#
    def get_details(self):
        return f"Бытовая химия: {self.name}, Объем: {self.volume} мл, Цена: {self.price} руб."