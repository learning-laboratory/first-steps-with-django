from django.contrib import admin
from .models import Product
# Register your models here to show in dashboard menu


admin.site.register(Product)
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display("name", "description", "price")