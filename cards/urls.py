from django.urls import path
from cards.views import cards_list

urlpatterns = [
    path("", cards_list, name="cards_list"),
]
