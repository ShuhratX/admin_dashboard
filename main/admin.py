from django.contrib import admin
from django.contrib.auth.models import Group, User
from modeltranslation.admin import TranslationAdmin
from .models import Product, Category
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'price', 'created_at')
    list_filter = ('name', 'price', 'created_at')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)