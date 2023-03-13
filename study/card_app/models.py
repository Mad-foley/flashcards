from django.db import models
from category.models import Categorie

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

class Category(models.Model):
    name = models.CharField(max_length=100)
    subject= models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    studied = models.BooleanField(default=False)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="student",
        on_delete=models.CASCADE,
        null=True
    )
    def __str__(self):
        return self.name
