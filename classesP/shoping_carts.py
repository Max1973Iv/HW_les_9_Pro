# 3. Класс для управления корзиной покупок
from datetime import datetime
class ShoppingCart:
    """
    Класс, представляющий корзину покупок.
    """
    def __init__(self,buyer=None, employee=None):
        self.items = []
        self.buyer = buyer  # Информация о покупателе
        self.employee = employee  # Информация о сотруднике магазина, который обслуживает покупателя
#
    def add_item(self, product, quantity):
        """
        Добавляет продукт в корзину.
        """
        self.items.append({"Продукт": product, "количество": quantity})
# информация о времени и дате создания корзины
    def creation_time(self):
        """ Возвращает дату и время создания заказа.
        """
        # Используем текущую дату и время для создания корзины  
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#
    def remove_item(self, product_name):
        """
        Удаляет продукт из корзины по имени.
        """
        self.items = [item for item in self.items if item["Продукт"].name != product_name]
#
    def get_total(self):
        """
        Возвращает общую стоимость продуктов в корзине.
        """
        total = sum(item["Продукт"].price * item["количество"] for item in self.items)
        return total
#
    def get_details(self):
        """
        Возвращает детализированную информацию о покупателе, содержимом корзины,
        общей стоимости и сотруднике магазина.
        """
#добавляем информацию о покупателе
        if self.buyer:
            details = f"{self.buyer.get_details()}\n"
        else:
            details = "Неизвестный\n"#если покупатель не указан
#
#добавляем информацию о корзине
        details += f"Корзина покупок:\n"
        if not self.items:
            details += "Корзина пуста.\n"# если корзина пуста
            return details
#добавляем информацию о каждом продукте в корзине
        for item in self.items:
            details += f"{item['Продукт'].get_details()}, Количество: {item['количество']}\n"
        details += f"Стоимость заказа в корзине: {self.get_total()} руб\n"
#добавляем информацию о сотруднике
        if self.employee:
            details += f"Оформил заказ: {self.employee.get_details()}\n"
        else:
            details += "Оформил заказ: Неизвестный\n"# если сотрудник не указан
#возвращаем детализированную информацию о корзине
        return details