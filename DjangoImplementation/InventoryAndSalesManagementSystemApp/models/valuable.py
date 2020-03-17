#-*- coding: utf-8 -*-
import uuid

from django.db import models

class Valuable(models.Model):
    class Meta:
        pass

    name = models.CharField(max_length=1024)
    price = models.FloatField()
    stock = models.IntegerField(default=0)
    serial = models.UUIDField(primary_key=True)


    def save(self, *args, **kwargs):
        if not self.serial:
            self.serial = uuid.uuid4()
        super().save(*args, **kwargs)

    def get_dict(self, ):
        return {
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "serial": self.serial
        }

