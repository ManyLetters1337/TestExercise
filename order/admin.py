from django.contrib import admin
from .models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    """
    Order Item Class
    """
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    """
    Order Admin Class
    """
    list_display = ['id', 'phone', 'first_name', 'last_name', 'address', 'city']

    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
