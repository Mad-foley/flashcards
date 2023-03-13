from django.urls import path
from card_app.views import create_card, edit_card

urlpatterns = [
    path("create/", create_card, name="create_card"),
    path("<int:id>/edit/", edit_card, name="edit_card")
]
