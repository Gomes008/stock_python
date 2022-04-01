from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    quantidade = models.IntegerField()
    valor = models.IntegerField()
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'produto'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
