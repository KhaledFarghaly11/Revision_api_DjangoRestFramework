from .models import  DetailsTask, NewPartner,Employee, Tasks, DetailsPartner, Partner
from .serializers import  DetailsTaskSerializer, NewPartnerSerializer, TasksSerializer, DetailsPartnerSerializer, EmployeeSerializer, PartnerSerializer

from rest_framework import viewsets


class viewsets_Employee(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class viewsets_Tasks(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

class viewsets_DetailsTask(viewsets.ModelViewSet):
    queryset = DetailsTask.objects.all()
    serializer_class = DetailsTaskSerializer

class viewsets_DetailsPartner(viewsets.ModelViewSet):
    queryset = DetailsPartner.objects.all()
    serializer_class = DetailsPartnerSerializer

class viewsets_Partner(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer



class viewsets_NewPartner(viewsets.ModelViewSet):
    queryset = NewPartner.objects.all()
    serializer_class = NewPartnerSerializer


