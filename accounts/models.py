from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from gifts.models import Gift

class UserInfo(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_info")
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)

    gender_choices = [
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('O', 'Outro'),
    ]
    gender = models.CharField(
        max_length=1,
        choices=gender_choices
    )

    size_choices = [
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
    ]
    size = models.CharField(
        max_length=1,
        choices=size_choices
    )

    style_choices = [
        ('BA', 'Básico'),
        ('MO', 'Moderninho'),
        ('EL', 'Elegante'),
    ]
    style = models.CharField(
        max_length=2,
        choices=style_choices
    )
    roupas = models.IntegerField()
    fitness = models.IntegerField()
    beleza = models.IntegerField()
    eletronicos = models.IntegerField()
    outros = models.IntegerField()

    friends = models.ManyToManyField("UserInfo", blank = True)

    likes = models.ManyToManyField(Gift, blank=True)
    def __str__(self):
        return self.user.username + str(' info')
