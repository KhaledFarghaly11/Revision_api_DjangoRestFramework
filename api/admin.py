from django.contrib import admin
from .models import  DetailsTask, NewPartner, Employee, Tasks, DetailsPartner, Partner

# Register your models here.

admin.site.register(Employee)
admin.site.register(Tasks)
admin.site.register(DetailsTask)
admin.site.register(DetailsPartner)
admin.site.register(Partner)
admin.site.register(NewPartner)



