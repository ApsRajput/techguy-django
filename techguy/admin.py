from django.contrib import admin

# Register your models here.
from techguy.models import Techguy, Category, Customer

class TechguyAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    # list_filter = ("status",)
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Techguy, TechguyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer)