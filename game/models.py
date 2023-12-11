from django.db import models  # F401


# Create your models here.
class Attempt(models.Model):
    word = models.CharField(max_length=5)

    def __str__(self) -> str:
        return self.word
