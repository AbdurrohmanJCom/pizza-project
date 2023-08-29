from django.db import models

# Create your models here.
class RegularPizza(models.Model):
    name = models.CharField(max_length=15)
    small = models.CharField(max_length=5)
    large = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.name} {self.small} {self.large}"


class SicilianPizza(models.Model):
    name = models.CharField(max_length=15)
    small = models.CharField(max_length=5)
    large = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.name} {self.small} {self.large}"


class Toppings(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Toppings"
    
    def __str__(self):
        return f"{self.name}"


class Subs(models.Model):
    name = models.CharField(max_length=60)
    small = models.CharField(max_length=5)
    large = models.CharField(max_length=5)

    class Meta:
        verbose_name_plural = "Subs"

    def __str__(self):
        return f"{self.name} {self.small} {self.large}"


class Pasta(models.Model):
    name = models.CharField(max_length=40)
    price = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.name} {self.price}"


class Salads(models.Model):
    name = models.CharField(max_length=40)
    price = models.CharField(max_length=5)

    class Meta:
        verbose_name_plural = "Salads"

    def __str__(self):
        return f"{self.name} {self.price}"

 
class DinnerPlatters(models.Model):
    name = models.CharField(max_length=40)
    small = models.CharField(max_length=5)
    large = models.CharField(max_length=5)

    class Meta:
        verbose_name_plural = "DinnerPlatters"

    def __str__(self):
        return f"{self.name} {self.small} {self.large}"


class ShoppingCart(models.Model):
    username = models.CharField(max_length=25)
    order = models.CharField(max_length=100)
    price = models.FloatField(blank=True, null=True)
    toppingsList = models.CharField(max_length=100, default="")
    approved = models.CharField(max_length=10, default="None")

    def __str__(self):
        return f"{self.username} {self.order} {self.price} {self.approved}"
