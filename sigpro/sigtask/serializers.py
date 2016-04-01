__author__ = 'Administrator'

from rest_framework import serializers
from sigtask.models import Musician, Album

class MusicianSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Musician
        fields = ('First_name','Last_name','Instrument')

class AlbumSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ('Artist','Name','Release_date','Num_starts')

