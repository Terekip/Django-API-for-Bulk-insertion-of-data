from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    image=models.CharField(max_length=255)

class ProductVariant(models.Model):
    product=models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    sku=models.CharField(max_length=255)
    name= models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    details=models.TextField()
