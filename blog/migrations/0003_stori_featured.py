# Generated by Django 4.1.3 on 2024-03-06 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="stori",
            name="featured",
            field=models.BooleanField(default=False),
        ),
    ]