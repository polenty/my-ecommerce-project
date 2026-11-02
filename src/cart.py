# Промокоды: код -> скидка в процентах
PROMO_CODES = {"SAVE10": 10, "SAVE20": 20, "SAVE50": 50}


class ShoppingCart:
    def __init__(self, products):
        # словарь: id товара -> товар
        self.products = {p.id: p for p in products}
        # корзина: id товара -> количество
        self.items = {}

    def add_item(self, product_id, quantity):
        """Добавить товар в корзину."""
        if quantity <= 0:
            raise ValueError("Количество должно быть больше 0")
        if product_id not in self.products:
            raise ValueError("Такого товара нет")

        new_quantity = self.items.get(product_id, 0) + quantity
        if new_quantity > self.products[product_id].stock:
            raise ValueError("Недостаточно товара на складе")

        self.items[product_id] = new_quantity

    def remove_item(self, product_id, quantity=None):
        """Убрать товар: quantity штук или полностью, если quantity не указано."""
        if product_id not in self.items:
            raise ValueError("Этого товара нет в корзине")
        if quantity is not None and quantity <= 0:
            raise ValueError("Количество должно быть больше 0")

        # убрать всё (или больше, чем есть) -> удаляем позицию целиком
        if quantity is None or quantity >= self.items[product_id]:
            del self.items[product_id]
        else:
            self.items[product_id] -= quantity

    def get_total(self, promo_code=None):
        """Стоимость корзины, со скидкой, если указан промокод."""
        total = 0
        for product_id, quantity in self.items.items():
            total += self.products[product_id].price * quantity

        if promo_code:
            if promo_code not in PROMO_CODES:
                raise ValueError("Неверный промокод")
            total = total * (100 - PROMO_CODES[promo_code]) / 100

        return round(total, 2)