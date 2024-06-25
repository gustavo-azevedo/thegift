# Generated by Django 5.0.6 on 2024-06-20 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_remove_userinfo_genero"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="style",
            field=models.CharField(
                choices=[("BA", "Básico"), ("MO", "Moderninho"), ("EL", "Elegante")],
                max_length=2,
            ),
        ),
    ]
