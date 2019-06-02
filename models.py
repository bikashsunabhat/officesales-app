from django.db import models
from datetime import datetime
class Branches(models.Model):
    bid=models.CharField(max_length=20)
    bname=models.CharField(max_length=100)
    salesamount=models.IntegerField(default=0)
    year=models.DateField()
    def yearpublished(self):
       return self.year.strftime('%Y')

    class Meta:
        db_table="salesactivity"


# Create your models here.

