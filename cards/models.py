from django.db import models
from categories.models import Categorie

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)

# Create your models here.
class Card(models.Model):
    term = models.CharField(max_length=250)
    answer = models.TextField()
    img = models.URLField(blank=True)
    box = models.IntegerField(
        choices=zip(BOXES, BOXES),
        default=BOXES[0],
    )
    category = models.ForeignKey(
        Categorie,
        related_name="cards",
        on_delete=models.CASCADE,
    )
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.term
