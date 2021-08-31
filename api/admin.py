from django.contrib import admin
from .models import  NewPartener, Employee, Tasks, Details, Partener

# Register your models here.

admin.site.register(Employee)
admin.site.register(Tasks)
admin.site.register(Details)
admin.site.register(Partener)
admin.site.register(NewPartener)



