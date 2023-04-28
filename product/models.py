from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    """
    Model for Product
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:product_detail', args=[self.id,])

