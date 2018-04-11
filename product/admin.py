from django.contrib import admin
from .models import TypeProduct, Product


class AdminTypeProduct(admin.ModelAdmin):
    list_display = ['category', 'slug_category']
    ordering = ['category']


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'stock', 'get_category']
    search_fields = ['name', 'description']
    list_per_page = 20
    list_filter = ['type_product__category']
    ordering = ['name']
    autocomplete_lookup_fields = {
        'name': ['name'],
        'description': ['description'],
    }

    def get_category(self, obj):
        return obj.type_product.category

    get_category.short_description = 'Categoria'
    get_category.admin_order_field = 'type_product__category'


admin.site.register(TypeProduct, AdminTypeProduct)
admin.site.register(Product, AdminProduct)
