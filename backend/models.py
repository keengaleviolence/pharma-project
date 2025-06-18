from django.db import models

class Product(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание", blank=True)

    def __str__(self):
        return self.name

class Batch(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField("Статус", max_length=20, default="В производстве")

    def __str__(self):
        return f"Партия #{self.id} - {self.product.name}"