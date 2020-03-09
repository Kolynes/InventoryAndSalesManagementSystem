#-*- coding: utf-8 -*-

from django.db import models

class Valuable(models.Model):
    class Meta:
        pass

    name = models.CharField(max_length=1024)
    price = models.FloatField()
    stock = models.IntegerField()
    serial = models.CharField(max_length=12, pk=True)


    def save(self, *args, **kwargs):
        pass

    def get_dict(self, ):
        pass

