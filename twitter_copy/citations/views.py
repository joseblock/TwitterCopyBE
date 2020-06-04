from rest_framework import viewsets
from citations.models import Cita
from citations.serialzers import CitaSerializer
from permissions.services import APIPermissionClassFactory

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer
    #TODO Permissons...
