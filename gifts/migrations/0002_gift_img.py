# Generated by Django 5.0.6 on 2024-06-19 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gifts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="gift",
            name="img",
            field=models.CharField(default="aa", max_length=300),
            preserve_default=False,
        ),
    ]
