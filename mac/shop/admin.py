from django.contrib import admin

# Register your models here.
from .models import Product, Contacts, Orders, OrderUpdate

admin.site.register(Product)
admin.site.register(Contacts)
admin.site.register(Orders)
admin.site.register(OrderUpdate)