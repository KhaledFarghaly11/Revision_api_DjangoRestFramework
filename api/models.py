from django.db import models
# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=250, null=True,blank=True)
    number = models.IntegerField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)

    def __str__(self):
        return self.name

class Details(models.Model):
    text_1 = models.CharField(max_length=250, default=True)
    text_2 = models.CharField(max_length=250, default=True)
    iconName = models.CharField(max_length=250, null=True,blank=True)

    def __str__(self):
        return self.iconName

class Tasks(models.Model):
    name = models.CharField(max_length=250, default=True)
    description = models.TextField(default=True)
    assignedTo = models.ManyToManyField(Employee, blank=True)
    amountDue = models.CharField(max_length=250, default=True)
    dueDate = models.CharField(max_length=250, default=True)
    isCompleted = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Partener(models.Model):
    name = models.CharField(max_length=250, default=True)
    description = models.TextField(default=True)
    details = models.ManyToManyField(Details, related_name='partener')
    tasks = models.ManyToManyField(Tasks)
    

    def __str__(self):
        return self.name

class NewPartener(models.Model):
    name = models.CharField(max_length=250, default=True)
    description = models.TextField(default=True)
    name2 = models.CharField(max_length=250, default=True)
    name3 = models.CharField(max_length=250, default=True)
    name4 = models.CharField(max_length=250, default=True)
    name5 = models.CharField(max_length=250, default=True)
    name6 = models.CharField(max_length=250, default=True)
    name7 = models.CharField(max_length=250, default=True)
    

    def __str__(self):
        return self.name

