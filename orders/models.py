from django.db import models
from myshop.models import Product


class Order(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    email = models.EmailField("Email")
    address = models.CharField("Адрес", max_length=250)
    postal_code = models.CharField("Индекс", max_length=20)
    city = models.CharField("Город", max_length=100)

    created = models.DateTimeField("Создан", auto_now_add=True)
    updated = models.DateTimeField("Обновлён", auto_now=True)
    paid = models.BooleanField("Оплачен", default=False)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Order #{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="order_items", on_delete=models.PROTECT)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField("Кол-во", default=1)

    class Meta:
        verbose_name = "Позиция заказа"
        verbose_name_plural = "Позиции заказа"

    def __str__(self):
        return str(self.id)
