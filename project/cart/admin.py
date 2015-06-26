from django.contrib import admin
from project.cart.models import CartItem, Order, Delivery

# Register your models here.
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(Delivery)