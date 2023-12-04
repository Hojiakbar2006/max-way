from django.db import models
from django.utils import timezone


class Category(models.Model):
    category = models.CharField(max_length=100, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.category


class Product(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    image = models.ImageField(upload_to='images', null=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    # def __str__(self):
    #     return self.title
    

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.IntegerField(null=False, blank=False)
    chat_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.first_name


class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=300, null=False, blank=False)
    

    # def __str__(self):
    #     return self.user,


class Order_product(models.Model):
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(null=False, blank=False)

    # def __str__(self):
    #     return self.product
