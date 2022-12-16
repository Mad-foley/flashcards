from django.urls import path, include
from categories.views import list_categories, show_set, create_set

urlpatterns = [
    path("", list_categories, name="list_categories"),
    path("<int:id>/", show_set, name="show_set"),
    path("create/", create_set, name="create_set"),
]
