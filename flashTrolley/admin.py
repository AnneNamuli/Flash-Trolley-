from django.contrib import admin
from .models import Customer, Product


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_image', 'product_description', 'product_price', 'expiry_date']
    list_filter = ['expiry_date']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'birth_date', 'email']
    search_fields = ['fname']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
