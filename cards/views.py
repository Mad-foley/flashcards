from django.shortcuts import render, redirect, get_object_or_404
from categories.models import Categorie
from cards.forms import CardForm
from cards.models import Card
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
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

@login_required
def edit_card(request, id):
    card = get_object_or_404(Card, id=id)
    if request.method == "POST":
        form = CardForm(request.POST, instance = card)
        if form.is_valid():
            form.save()
            return redirect("show_set", card.category.id)
    else:
        form = CardForm(instance = card)

    context = {
        "card_object": card,
        "card_form": form,
    }
    return render(request, "cards/edit.html", context)
