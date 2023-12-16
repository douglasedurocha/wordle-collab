from django.contrib import admin  # F401
from .models import CustomUser

# Register your models here.
admin.site.register(CustomUser)
