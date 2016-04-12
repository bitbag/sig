#coding:GBK
from sigtask.models import *


def CreateMission():
    if request.method == 'GET':
        return render(request,'create_mission.html')
    elif request.method == 'POST':
        try:
            HostList = list(set([ x for x in request.REQUEST.get('hostlist').split(',')]))
            PlaybookList = list(set([y for y in request.REQUEST.get('playbook').split(',')]))
            MissionVersion = request.REQUEST.get('missversion')
            try:
                print r'======================开始生成主任务==================='
                Musician.objects.create(First_name=HostList,Last_name=PlaybookList,Instrument=MissionVersion)
                print '======================主任务已生成====================='
            except Exception,error:
                print '====================Create mission failed! %s======================' % error
        except Exception,error:
            print '===============No host or playbook selected! %s==========================' % error
        return render(request,'basex.html',{'sdf':(PlaybookList,HostList,MissionVersion)})
