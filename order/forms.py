from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    """
    Order Creation Form Class
    """
    class Meta:
        model = Order
        fields = ['phone', 'first_name', 'last_name', 'address', 'city']

