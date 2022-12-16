from django.db import models
from categories.models import Categorie

# Create your models here.
class Card(models.Model):
    term = models.CharField(max_length=250)
    answer = models.TextField()
    img = models.URLField(null=True)
    category = models.ForeignKey(
        Categorie,
        related_name="cards",
        on_delete=models.CASCADE,
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.term
