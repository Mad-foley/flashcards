from django.db import models
from django.conf import settings

# Create your models here.
class Categorie(models.Model):
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
