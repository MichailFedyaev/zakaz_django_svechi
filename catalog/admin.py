from django.contrib import admin
from .models import Candles


@admin.register(Candles)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity', 'image')
    list_filter = ('price', 'quantity')
    search_fields = ('name', 'price')
