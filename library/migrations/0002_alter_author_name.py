# Generated by Django 5.0.6 on 2024-06-10 06:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
