from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now



# Create your models here.


class Expense(models.Model):
    amount = models.FloatField()
    date = models.DateField(default=now)
    description = models.TextField()
    ncompra = models.TextField(max_length=255, default='Desconocido')
    dfactura = models.CharField(max_length=255, default='Desconocido')
    ddespacho = models.CharField(max_length=255, default='Desconocido')
    contacto = models.CharField(max_length=255, default='Desconocido')
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models.CharField(max_length=266)

    def __str__(self):
        return self.category

    class Meta:
        ordering: ['-date']


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
