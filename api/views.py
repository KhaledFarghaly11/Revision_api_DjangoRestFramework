from .models import  NewPartener,Employee, Tasks, Details, Partener
from .serializers import  NewPartenerSerializer, TasksSerializer, DetailsSerializer, EmployeeSerializer, PartenerSerializer

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

class viewsets_Partener(viewsets.ModelViewSet):
    queryset = Partener.objects.all()
    serializer_class = PartenerSerializer



class viewsets_NewPartener(viewsets.ModelViewSet):
    queryset = NewPartener.objects.all()
    serializer_class = NewPartenerSerializer


