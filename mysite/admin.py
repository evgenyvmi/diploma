from django.contrib import admin

from .models import Order
from .models import Client
from .models import Product
from .models import Category
from .models import Order_product
# Register your models here.

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Category)
admin.site.register(Order_product)