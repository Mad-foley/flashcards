from django.urls import path
from cards.views import cards_list

urlspatterns = [
    path("", cards_list, name="cards_list")
]
