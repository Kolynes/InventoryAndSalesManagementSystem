#-*- coding: utf-8 -*-

from django.db import models
import json

class Action(models.Model):
    """This class is used to store a chronology of actions made on the application."""
    class Meta:
        pass

    VALUABLE_CREATED = "VCR"
    VALUABLE_DELETED = "VDE"
    VALUABLE_STOCKED = "VST"
    VALUABLE_DESTOCKED = "VDS"
    VALUABLE_RENAMED = "VRE"
    VALUABLE_PRICE_CHANGED = "VPC"
    VALUABLE_SOLD = "VSO"
    TYPES = (
        (VALUABLE_CREATED, "Valuable Created"),
        (VALUABLE_DELETED, "Valuable Deleted"),
        (VALUABLE_STOCKED, "Valuable Stocked"),
        (VALUABLE_RENAMED, "Valuable Renamed"),
        (VALUABLE_PRICE_CHANGED, "Valuable Price Changed"),
        (VALUABLE_SOLD, "Valuable Sold")
    )

    type = models.CharField(max_length=3, choices=TYPES)
    date = models.DateTimeField(auto_now_add=True)
    valuable_snapshot = models.TextField()
    
    valuable = models.ForeignKey('Valuable', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('User', on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        if not self.valuable_snapshot:
            self.valuable_snapshot = json.dumps(self.valuable.get_dict())
        super().save(*args, *kwargs)
        
    def get_dict(self, ):
        return {
            "type": self.get_type_display(),
            "date": self.date.timestamp() * 1000,
            "user": self.user.get_dict(),
            "valuable": json.loads(self.valuable_snapshot)
        }

