#-*- coding: utf-8 -*-

from django.db import models

class Demand(models.Model):
    class Meta:
        pass

    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    valuable = models.ForeignKey('Valuable', on_delete=models.CASCADE)

    def get_dict(self, ):
        return {
            "quantity": self.quantity,
            "date": self.date.timestamp() * 1000,
            "valuable": self.valuable.get_dict()
        }

