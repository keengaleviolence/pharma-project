from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, default="В обработке")

class QualityCheck(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    passed = models.BooleanField(default=False)
    notes = models.TextField(blank=True)