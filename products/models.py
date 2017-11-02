from django.db import models

# Create your models here.


class Supplier(models.Model):
    name = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=200)
    e_mail = models.EmailField()
    contact_person_first_name = models.CharField(max_length=50)
    contact_person_last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity_in_stock = models.DecimalField(default=0, decimal_places=0, max_digits=10)
    reorder_level = models.DecimalField(default=50, decimal_places=0, max_digits=10)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=None)
    supplier = models.ManyToManyField(Supplier)

    def __str__(self):
        return self.name






