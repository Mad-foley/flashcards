from django.forms import ModelForm
from card_app.models import Card

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = [
            "term",
            "answer",
            "img",
            "category",
        ]
