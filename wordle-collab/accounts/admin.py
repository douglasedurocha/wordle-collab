from django.contrib import admin  # F401
from .models import Player

# Register your models here.
admin.site.register(Player)
