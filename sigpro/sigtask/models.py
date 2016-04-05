from django.db import models

# Create your models here.
class  Musician(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Instrument = models.CharField(max_length=100)

class Album(models.Model):
    Artist = models.ForeignKey(Musician)
    Name = models.CharField(max_length=100)
    Release_date = models.DateField()
    Num_starts = models.IntegerField()


class Services(models.Model):
    serviceid = models.CharField(max_length=15)
    servicename = models.CharField(max_length=30)
    serviceversion = models.CharField(max_length=30)
    serviceport = models.IntegerField()
