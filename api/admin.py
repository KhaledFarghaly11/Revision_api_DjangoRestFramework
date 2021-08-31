from django.contrib import admin
from .models import  NewPartner, Employee, Tasks, Details, Partner

# Register your models here.

admin.site.register(Employee)
admin.site.register(Tasks)
admin.site.register(Details)
admin.site.register(Partner)
admin.site.register(NewPartner)



