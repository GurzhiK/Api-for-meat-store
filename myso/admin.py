from django.contrib import admin
from .models import User, Product, Order, OrderDetail, ShoppingCart

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(User)
admin.site.register(ShoppingCart)
