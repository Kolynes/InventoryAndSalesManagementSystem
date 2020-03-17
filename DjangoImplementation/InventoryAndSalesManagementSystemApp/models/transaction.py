#-*- coding: utf-8 -*-

from django.db import models
import json

class Transaction(models.Model):
    class Meta:
        ordering = ["-date"]

    SALE = "S"
    PURCHASE = "P"
    TYPES = (
        (PURCHASE, "Purchase"), 
        (SALE, "Sale")
    )
    quantity = models.IntegerField()
    amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=1, choices=TYPES)
    valuable_snapshot = models.TextField()

    valuable = models.ForeignKey('Valuable', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('User', on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        if not self.valuable_snapshot:
            self.valuable_snapshot = json.dumps(self.valuable.get_dict())
        super().save(*args, *kwargs)

    def get_dict(self, ):
        return {
            "quantity": self.quantity,
            "amount": self.amount,
            "date": self.date.timestamp() * 1000,
            "type": self.get_type_display(),
            "valuable": json.loads(self.valuable_snapshot),
            "user": self.user.get_dict()
        }

