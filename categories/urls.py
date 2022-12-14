from django.urls import path, include
from categories.views import list_categories, show_set, edit_card, create_card

urlpatterns = [
    path("", list_categories, name="list_categories"),
    path("<int:id>/", show_set, name="show_set"),
    path("<int:id>/edit/", edit_card, name="edit_card"),
    path("create/", create_card, name="create_card"),
]
