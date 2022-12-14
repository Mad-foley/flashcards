from django.forms import ModelForm
from categories.models import Card, Categorie

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = [
            "term",
            "answer",
            "img",
            "category",
        ]

class CategorieForm:
    class Meta:
        model = Categorie
        fields = [
            "name",
            "subject",
        ]
