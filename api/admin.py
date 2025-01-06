from django.contrib import admin
from . models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("ar_no", "id", "link", "area", "abnormality", "ar_category", "nature_of_abnormality", "affected_item", "level", "created", "detection_process", "function", "incharge", "self_resolve_for_car", "status", "countermeasure", "fanout", "remarks", "timestamp")

# Register your models here.
admin.site.register(Category, CategoryAdmin)