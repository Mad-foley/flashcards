from django.contrib import admin
from categories.models import Categorie, Card

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

@admin.register(Card)
class Card(admin.ModelAdmin):
    list_display = [
        "term",
        "answer",
        "img",
        "category",
        "date_created",
    ]
