from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=250, default="")
    address = models.CharField(max_length=500, default="")
    username = models.CharField(max_length=100, default="")
    is_login = models.BooleanField(default=False)

    def __str__ (self):
        return self.username
"""
class Menu(models.Model):
    menu = models.CharField(max_length=10)
    price =  .PositiveIntegerField()

    def __str__ (self):
        return self.menu + " --- Php." + str(self.price) + ".00"
"""

class Order(models.Model):
    username = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity_chicken = models.PositiveIntegerField(default=0)
    quantity_fries = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "History"