from rest_framework import serializers
from .models import  NewPartner,  Tasks, Partner, Details, Employee



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

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"
        depth = 1
        


class NewPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewPartner
        fields = '__all__'



        