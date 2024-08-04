from django.contrib import admin
from .models import Product, Review

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)  # Только одна регистрация с указанием класса ProductAdmin
admin.site.register(Review)
