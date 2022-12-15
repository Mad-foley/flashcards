from django.shortcuts import render, redirect, get_object_or_404
from categories.models import Categorie, Card
from categories.forms import CardForm
from django.views.generic import ListView

# Create your views here.
def list_categories(request):
    category = Categorie.objects.all()
    context = {
        "category_list": category,
    }
    return render(request, "categories/list.html", context)

def show_set(request, id):
    set = Card.objects.filter(category=id)
    category = get_object_or_404(Categorie, id=id)
    context = {
        "set": set,
        "category": category,
    }
    return render(request, "categories/set.html", context)

def create_card(request):
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CardForm()

    context = {
        "form" : form,
    }
    return render(request, "cards/create.html", context)


def edit_card(request, id):
    card = get_object_or_404(Card, id=id)
    if request.method == "POST":
        form = CardForm(request.POST, instance = card)
        if form.is_valid():
            form.save()
            return redirect("show_set", id=card.category.id)
    else:
        form = CardForm(instance = card)

    context = {
        "card_object": card,
        "card_form": form,
    }
    return render(request, "cards/edit.html", context)
