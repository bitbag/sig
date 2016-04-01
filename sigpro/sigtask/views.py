from django.shortcuts import render_to_response
from sigtask.models import Musician, Album
from rest_framework import viewsets
from sigtask.serializers import MusicanSerialize, AlbumSerialize
# Create your views here.

class MusicanViewset(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicanSerialize

class AlbumViewset(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerialize

def index(request):
    author_list = Musician.objects.all().values()
    return render_to_response('basex.html',{'sdf':author_list})
