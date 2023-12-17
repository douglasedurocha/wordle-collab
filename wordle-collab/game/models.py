from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Game(models.Model):
    STATUS_CHOICES = [
        ("W", "Waiting"),
        ("A", "Active"),
        ("C", "Completed"),
    ]

    word = models.CharField(max_length=5)
    players = models.ManyToManyField(User)
    max_players = models.IntegerField(default=2)
    max_attempts = models.IntegerField(default=5)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="W")

    def add_player(self, player):
        if self.players.count() >= self.max_players:
            return
        self.players.add(player)
        self.save()
        return


# Create your models here.
class Attempt(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.CharField(max_length=5)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.word
