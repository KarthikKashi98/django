from __future__ import unicode_literals
from django.db import models


class sampleTable(models.Model):

    parking_slotname=models.CharField(max_length=20,primary_key=True)
    parking_floor=models.IntegerField()
    parking_nearest=models.CharField(max_length=30,default="north")

    def  save(self, *args,**kwargs):
        return super(sampleTable, self).save(*args,**kwargs)


    def __unicode__(self):
        return str(self.id)


    class Meta:
        db_table="Parking"
        app_label="assignment1"