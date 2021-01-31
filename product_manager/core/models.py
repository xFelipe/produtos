from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Product(models.Model):
    name = models.CharField('nome', max_length=255)
    description = models.TextField('descricao', blank=True)
    value = models.DecimalField('valor', max_digits=15, decimal_places=2,
                                validators=[MinValueValidator(0)])
