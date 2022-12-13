from django.shortcuts import render
from cards.models import Card
from django.views.generic import ListView


# class CardListView(ListView):
#     model = Card
#     queryset = Card.objects.all().order_by("box", "subject")
# Create your views here.
def cards_list(request,id):
    pass
