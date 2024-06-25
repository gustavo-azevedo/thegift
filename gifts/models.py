from django.db import models
class Gift(models.Model):
    name = models.CharField(max_length=52)
    loja = models.CharField(max_length=300)
    img = models.CharField(max_length=300)
    cat = models.CharField(max_length=20)
    

    def __str__(self):
        return f'{self.name}'