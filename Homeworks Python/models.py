from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Filial(models.Model):
    full_address = models.CharField(max_length=255)
    short_address = models.CharField(max_length=32)


class Department(models.Model):
    name = models.CharField(max_length=255)
    floor = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    filial = models.ForeignKey(
        'company.Filial',
        null=True,
        related_name='departments',
        on_delete=models.PROTECT,
    )


class Employee(models.Model):
    full_name = models.CharField(max_length= 64)
    post = models.CharField(max_length=64)
    telephone = models.CharField(max_length=32, null=True)
    birthday = models.DateField(null=True)
    email = models.EmailField(null=True)
    department = models.ForeignKey(
        'company.Department',
        null=True,
        related_name='employees',
        on_delete=models.CASCADE,
    )