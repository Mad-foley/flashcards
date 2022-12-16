from django.forms import ModelForm
from categories.models import Categorie


class CategorieForm(ModelForm):
    class Meta:
        model = Categorie
        fields = [
            "name",
            "subject",
        ]
