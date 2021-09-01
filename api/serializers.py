from rest_framework import serializers
from .models import  DetailsTask, NewPartner,  Tasks, Partner, DetailsPartner, Employee



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
        depth = 1

class DetailsTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailsTask
        fields = '__all__'

class DetailsPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailsPartner
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



        