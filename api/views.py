from .models import  NewPartner,Employee, Tasks, Details, Partner
from .serializers import  NewPartnerSerializer, TasksSerializer, DetailsSerializer, EmployeeSerializer, PartnerSerializer

from rest_framework import viewsets


class viewsets_Employee(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class viewsets_Tasks(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

class viewsets_Details(viewsets.ModelViewSet):
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer

class viewsets_Partner(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer



class viewsets_NewPartner(viewsets.ModelViewSet):
    queryset = NewPartner.objects.all()
    serializer_class = NewPartnerSerializer


