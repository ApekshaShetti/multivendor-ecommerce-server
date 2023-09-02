from django.db import models
from django.contrib.auth.models import User

# Vendor Models
class Vendor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.user.username

# Product Category
class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title
    
# Products
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.title