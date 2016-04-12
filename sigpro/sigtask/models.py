from django.db import models
from django.contrib import admin

# Create your models here.
class  Musician(models.Model):
    Instrument_type = (
        ('p','piano'),
        ('v','violin'),
        ('g','guita'),
        ('c','cello'),
    )
    status_type = (
        ('0','unexecuted'),
        ('1','executing'),
        ('2','executed'),
        ('3','failed'),
        ('4','unknown'),
    )
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Instrument = models.CharField(max_length=100,choices=Instrument_type,verbose_name='ins_type')
    version = models.CharField(max_length=65,default=None)
    status = models.CharField(max_length=30,choices=status_type,default=4)
    def __unicode__(self):
        return self.version

class Album(models.Model):
    Artist = models.ForeignKey(Musician)
    Name = models.CharField(max_length=100)
    Release_date = models.DateField()
    Num_starts = models.IntegerField(default=2)
    status = models.CharField(max_length=30,default=None)
    def __unicode__(self):
        return self.Name


class Services(models.Model):
    serviceid = models.CharField(max_length=15)
    servicename = models.CharField(max_length=30)
    serviceversion = models.CharField(max_length=30)
    serviceport = models.IntegerField()
    def __unicode__(self):
        return self.serviceid



admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Services)