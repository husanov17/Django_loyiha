from django.contrib import admin
from .models import Product, Student, Course, Teacher
from unfold.admin import ModelAdmin

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Teacher)


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name',)
    list_display_links = ('name', 'price')
    list_filter = ('price',)

