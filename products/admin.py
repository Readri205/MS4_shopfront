from django.contrib import admin
from .models import Product, Type, Country, Appellation, Variety

# Register your models here.
admin.site.register(Product)
admin.site.register(Type)
admin.site.register(Country)
admin.site.register(Appellation)
admin.site.register(Variety)
