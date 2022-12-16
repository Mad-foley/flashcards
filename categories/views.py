from django.shortcuts import render, redirect, get_object_or_404
from categories.models import Categorie
from cards.models import Card
from categories.forms import CategorieForm
from django.contrib.auth.decorators import login_required


def list_categories(request):
    category = Categorie.objects.all()
    context = {
        "category_list": category,
    }
    return render(request, "categories/list.html", context)

@login_required
def show_set(request, id):
    set = get_object_or_404(Categorie, id=id)
    context = {
        "set": set,
    }
    return render(request, "categories/set.html", context)

@login_required
def create_set(request):
    if request.method == "POST":
        form = CategorieForm(request.POST)
        if form.is_valid():
            set = form.save(False)
            set.owner = request.user
            set.save()
            return redirect("home")
    else:
        form = CategorieForm()

    context = {
        "form": form,
    }
    return render(request, "categories/create.html", context)
