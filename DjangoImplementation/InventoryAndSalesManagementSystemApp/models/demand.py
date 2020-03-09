#-*- coding: utf-8 -*-

from django.db import models

class Demand(models.Model):
    class Meta:
        pass

    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now=True)


    def get_dict(self, ):
        pass

