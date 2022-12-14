from django.forms import ModelForm
from categories.models import Card

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = [
            "term",
            "answer",
            "img",
            "category",
        ]
