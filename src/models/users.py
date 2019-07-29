from django.db import models


class Users(models.Model):
    parking_slotname=models.CharField(max_length=20,primary_key=True)
    parking_floor=models.IntegerField()
    parking_nearest=models.CharField(max_length=30,default="north")


    def  save(self, *args,**kwargs):
        return super(Users, self).save(*args,**kwargs)


    def __unicode__(self):
        return str(self.id)


    class Meta:
        db_table="users"
        app_label="src"