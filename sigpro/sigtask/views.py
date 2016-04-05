from django.shortcuts import render_to_response, render
from sigtask.models import Musician, Album, Services
from rest_framework import viewsets
from sigtask.serializers import MusicianSerialize, AlbumSerialize, ServicesSerialize
from django.core.cache import cache
import logging,json

class MusicianViewset(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerialize


class AlbumViewset(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerialize

class ServicesViewset(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerialize

def index(request):
    return render(request,'index.html')



def Write_to_redis(request):
   dics = {}
    if request.method == 'POST':
        dics = eval(json.dumps(request.POST))
        try:
            for k,val in dics.items():
                print k,val
                if k != 'csrfmiddlewaretoken':
                    cache.set(k,val)
    return render(request,'basex.html',{'sdf':dics})

def Get_from_redis(request,*args):
    dicc = {}
    for i in args:
        try:
            dicc[i] = cache.get(i)
        except Exception,e:
            return render(request,'basex.html',{'sdf':e})
    return render(request,'basex.html',{'sdf':dicc})

def basex(request):
    dicx = {}
    if request.method == 'POST':
        dicx = eval(json.dumps(request.POST))
        try:
            for k,val in dicx.items():
                print k,val
                if k != 'csrfmiddlewaretoken':
                    cache.set(k,val)
        except Exception,e:
            return  render(request,'basex.html',{'sdf':e})
    return render(request,'basex.html',{'sdf':dicx})

