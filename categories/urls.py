from django.urls import path
from categories.views import list_categories

urlpatterns = [
    path("", list_categories, name="list_categories"),
]
