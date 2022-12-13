from django.contrib import admin
from categories.models import Categorie

# Register your models here.
@admin.register(Categorie)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "subject",
        "created_on",
        "owner",
        "studied",
    )
