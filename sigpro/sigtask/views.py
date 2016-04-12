#coding:GBK
from django.shortcuts import render_to_response, render
from sigtask.models import Musician, Album, Services
from rest_framework import viewsets
from sigtask.serializers import MusicianSerialize, AlbumSerialize, ServicesSerialize
from django.core.cache import cache
import logging,json
from rest_framework_filters import backends
import rest_framework_filters as filters
from .filters import *
from datetime import datetime

class MusicianViewset(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerialize
    filter_backends = (backends.DjangoFilterBackend, )
    filter_class = MusicianFilter


class AlbumViewset(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerialize
    filter_backends = (backends.DjangoFilterBackend, )
    filter_class = AlbumFilter

class ServicesViewset(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerialize
    filter_backends = (backends.DjangoFilterBackend, )
    filter_class = ServicesFilter

def index(request):
    return render(request,'index.html')

def CreateMission(request):
    if request.method == 'GET':
        return render(request,'create_mission.html')
    elif request.method == 'POST':
        try:
            HostList = list(set([ host for host in request.REQUEST.get('hostlist').split(',')]))
            PlaybookList = list(set([playbook for playbook in request.REQUEST.get('playbook').split(',')]))
            MissionVersion = request.REQUEST.get('missversion')
            versionid = datetime.now().strftime("%Y%m%d%H%M%S")
            status = {
                '0':'unexecuted',
                '1':'executing',
                '2':'executed',
                '3':'failed',
                '4':'unknown',
            }
            try:
                print r'=====================开始生成主任务==================='
                Musician.objects.create(First_name=HostList,Last_name=PlaybookList,Instrument=MissionVersion,version=versionid,status=status['0'])
                print '======================主任务已生成====================='
                if PlaybookList:
                    try:
                        for host in HostList:
                            Album.objects.create(Artist=Musician.objects.get(version=versionid),Name=PlaybookList,Release_date=datetime.now(),status=status['0'])
                        print '======================子任务已生成====================='
                    except Exception,error:
                        print "==============子任务生成失败 %s===================" % error
                else:
                    print "==================PlaybookList is Null============"
            except Exception,error:
                print '====================Create mission failed! %s======================' % error
        except Exception,error:
            print '===============No host or playbook selected! %s==========================' % error
        return render(request,'basex.html',{'sdf':(PlaybookList,HostList,MissionVersion)})

# def CreateSubMission(request):









def WriteToRedis(request):
    dics = {}
    if request.method == 'POST':
        dics = eval(json.dumps(request.POST))
        try:
            for k,val in dics.items():
                print k,val
                if k != 'csrfmiddlewaretoken':
                    cache.set(k,val)
        except Exception,e:
            return render(request,'basex.html',{'sdf':dics})

def GetFromRedis(request,*args):
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

