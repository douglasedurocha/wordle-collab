from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Game(models.Model):
    STATUS_CHOICES = [
        ("W", "Waiting"),
        ("A", "Active"),
        ("D", "Defeat"),
        ("V", "Victory"),
    ]

    word = models.CharField(max_length=5)
    players = models.ManyToManyField(User)
    max_players = models.IntegerField(default=2)
    max_attempts = models.IntegerField(default=5)
    turn = models.IntegerField(default=0)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="W")

    def add_player(self, player):
        if self.players.count() >= self.max_players:
            return
        self.players.add(player)
        self.save()
        return

    def remove_player(self, player):
        self.players.remove(player)
        self.save()
        return

    def next_turn(self):
        self.turn += 1
        self.turn = self.turn % self.players_count
        self.save()
        return

    @property
    def current_player(self):
        return self.players.all()[self.turn]

    @property
    def players_count(self):
        return self.players.count()

    @property
    def attempts_count(self):
        return self.attempt_set.count()

    @property
    def author_email(self):
        return self.players.first().email

    @property
    def is_over(self):
        return self.status == "D" or self.status == "V"


# Create your models here.
class Attempt(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.CharField(max_length=5)
    hint = models.CharField(max_length=5)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.word
