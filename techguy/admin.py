from django.contrib import admin

# Register your models here.
from techguy.models import *

class TechguyAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    # list_filter = ("status",)
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'product_type')
    # list_filter = ("status",)
    search_fields = ['name', 'product_type']

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'order_id', 'customer', 'status')
    # list_filter = ("status",)
    search_fields = ['order_id', 'status']

admin.site.register(Techguy, TechguyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)