from django.db import models
from categories.models import Categorie

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)

# Create your models here.
class Card(models.Model):
    term = models.TextField()
    answer = models.TextField()
    box = models.IntegerField(
        choices=zip(BOXES, BOXES),
        default=BOXES[0],
    )
    category = models.ForeignKey(
        Categorie,
        related_name="cards",
        on_delete=models.CASCADE,
    )
