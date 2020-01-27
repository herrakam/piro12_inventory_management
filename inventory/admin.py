from django.contrib import admin
from. import views
from .models import Product, Client

admin.site.register(Product)
admin.site.register(Client)
