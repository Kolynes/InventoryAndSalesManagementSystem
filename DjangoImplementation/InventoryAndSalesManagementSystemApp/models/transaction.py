#-*- coding: utf-8 -*-

from django.db import models

class Transaction(models.Model):
    class Meta:
        pass

    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    valuable = models.ForeignKey('Valuable', on_delete=models.PROTECT)

    def get_dict(self, ):
        pass

