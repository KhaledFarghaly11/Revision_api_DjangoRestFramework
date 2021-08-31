from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tasks', views.viewsets_Tasks)
router.register('details', views.viewsets_Details)
router.register('employee', views.viewsets_Employee)
router.register('partner', views.viewsets_Partner)
router.register('new', views.viewsets_NewPartner)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('content/', include(router.urls)),

]
