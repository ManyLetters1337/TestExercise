from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from product.models import Product
from shop import settings


class Order(models.Model):
    """
    Order Model
    """
    phone = PhoneNumberField(null=False, blank=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_price() for item in self.items.all())

    def save_user_info(self, request):
        request.session[settings.USER_INFO_SESSION_ID] = {'phone': str(self.phone), 'first_name': self.first_name,
                                                          'last_name': self.last_name, 'address': self.address,
                                                          'city': self.city}


class OrderItem(models.Model):
    """
    Order Item Model
    """
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '{}'.format(self.id)

    def get_price(self):
        return self.price
