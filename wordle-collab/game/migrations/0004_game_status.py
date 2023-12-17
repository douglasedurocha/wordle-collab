# Generated by Django 5.0 on 2023-12-17 01:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("game", "0003_rename_max_atempts_game_max_attempts"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="status",
            field=models.CharField(
                choices=[("W", "Waiting"), ("A", "Active"), ("C", "Completed")],
                default="W",
                max_length=1,
            ),
        ),
    ]