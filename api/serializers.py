from rest_framework import serializers
from .models import  NewPartener,  Tasks, Partener, Details, Employee



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'

class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = '__all__'

class PartenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partener
        fields = "__all__"
        depth = 1
        


class NewPartenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewPartener
        fields = '__all__'



        