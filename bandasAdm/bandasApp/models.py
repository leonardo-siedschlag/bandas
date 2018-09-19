from django.db import models


class CadastroBandas(models.Model):
    nomeBanda= models.CharField(max_length=128, unique=True)
    tempoCarreira = models.IntegerField(max_length = 30,null=True)
    dataFundacao = models.DateField(null=True)
    categoria = models.CharField(max_length = 128)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.nomeBanda

