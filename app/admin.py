from django.contrib import admin
from .models import (
    Customer,
    Product,
    Cart,
    OrderPlaced,
)


# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(OrderPlaced)
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'pincode', 'state']