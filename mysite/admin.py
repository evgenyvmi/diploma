from django.contrib import admin

from .models import Request
from .models import Client
from .models import Product
from .models import Category
# Register your models here.

admin.site.register(Request)
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Category)