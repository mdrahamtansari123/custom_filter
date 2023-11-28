

######### filter.py  ###########


import django_filters
from courses.models import *


class StandardFilter(django_filters.FilterSet):
    class Meta:
        model = Standard
        fields = {
            'id':  ['exact'],
            'standard_name': ['exact'],
        }



############ views.py ################
from courses.filters import StandardFilter
from rest_framework import filters
from courses.filters import StandardFilter

class StandardViewSet(CourseMixin):
    filter_fields = ["standard_name"]
    serializer_class = serializers.StandardSerializer
    filterset_class = StandardFilter