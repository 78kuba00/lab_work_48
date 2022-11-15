from django.contrib import admin
from webapp.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'details', 'status', 'balance', 'price']
    list_display_links = ['product']
    list_filter = ['status']
    search_fields = ['id']
    exclude = []

admin.site.register(Product, ProductAdmin)


# Register your models here.
