# Generated by Django 5.0.6 on 2024-06-20 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gifts", "0004_alter_gift_likes"),
    ]

    operations = [
        migrations.AddField(
            model_name="gift",
            name="cat",
            field=models.CharField(default="roupas", max_length=20),
            preserve_default=False,
        ),
    ]
