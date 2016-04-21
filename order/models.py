from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=250, default="")
    address = models.CharField(max_length=500, default="")
    username = models.CharField(max_length=100, default="")

    def __str__ (self):
        return self.name

class Menu(models.Model):
    menu = models.CharField(max_length=10)
    price = models.PositiveIntegerField()

    def __str__ (self):
        return self.menu + " --- Php." + str(self.price) + ".00"

class Order(models.Model):
    name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    orders = models.ForeignKey(Menu)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return "History"