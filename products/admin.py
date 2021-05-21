from django.contrib import admin
from .models import Product, Type, Country, Appellation, Variety

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'product',
        'type',
        'variety',
        'appellation',
        'country',
        'rating',
        'price',
        'image',
    )

    ordering = ('sku',)


class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'flag_url',
    )

    ordering = ('friendly_name',)


class VarietyAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


class AppellationAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Appellation, AppellationAdmin)
admin.site.register(Variety, VarietyAdmin)
