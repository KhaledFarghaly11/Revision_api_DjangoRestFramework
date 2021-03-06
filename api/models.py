from django.db import models
# Create your models here.

class Employee(models.Model):
    fullName = models.CharField(max_length=250, null=True,blank=True)
    number = models.IntegerField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class DetailsPartner(models.Model):
    text_1 = models.CharField(max_length=250)
    text_2 = models.CharField(max_length=250)
    iconName = models.CharField(max_length=250, null=True,blank=True)

    def __str__(self):
        return self.iconName

class DetailsTask(models.Model):
	Add_info_1 = models.CharField(max_length=100, default="")
	Add_info_2 = models.CharField(max_length=100, default="")
	Add_info_3 = models.CharField(max_length=100, default="")

class Tasks(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    assignedTo = models.ManyToManyField(Employee)
    amountDue = models.CharField(max_length=250)
    dueDate = models.CharField(max_length=250)
    isCompleted = models.BooleanField()
    details_tasks = models.ManyToManyField(DetailsTask, blank=True)

    def __str__(self):
        return self.name



class Partner(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    details = models.ManyToManyField(DetailsPartner, related_name='partner')
    tasks = models.ManyToManyField(Tasks, blank=True)
    

    def __str__(self):
        return self.name

class NewPartner(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    field1 = models.CharField(max_length=250)
    field2 = models.CharField(max_length=250)
    field3 = models.CharField(max_length=250)
    field4 = models.CharField(max_length=250)
    field5 = models.CharField(max_length=250)
    field6 = models.CharField(max_length=250)
    

    def __str__(self):
        return self.name

