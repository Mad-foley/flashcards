from django.contrib import admin
from cards.models import Card

# Register your models here.
@admin.register(Card)
class Card(admin.ModelAdmin):
    list_display = (
        "term",
        "answer",
        "img",
        "category",
        "date_created",
    )
