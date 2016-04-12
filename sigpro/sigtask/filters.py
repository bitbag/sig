import django_filters
from rest_framework_filters import filters
from rest_framework_filters.filters import RelatedFilter, AllLookupsFilter
from rest_framework_filters.filterset import FilterSet, LOOKUP_SEP
from sigtask.models import *

class MusicianFilter(django_filters.FilterSet):
    name  = filters.CharFilter(name='First_name')
    version = filters.CharFilter(name='version')
    status = filters.CharFilter(name='status')

    class Meta:
        model = Musician

class AlbumFilter(django_filters.FilterSet):
    name = filters.CharFilter(name='Name')

    class Meta:
        model = Album

class ServicesFilter(django_filters.FilterSet):
    serviceid = filters.CharFilter(name='serviceid')
    servicename = filters.CharFilter(name='servicename')

    class Meta:
        model = Services

