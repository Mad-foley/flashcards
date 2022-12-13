from django.shortcuts import render, redirect, get_object_or_404
from categories.models import Categorie

# Create your views here.
def list_categories(request):
    category = Categorie.objects.all()
    context = {
        "category_list": category,
    }
    return render(request, "categories/list.html", context)
