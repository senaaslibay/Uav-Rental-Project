from django.conf.urls import include
from django.urls import  re_path as url
from .views import *
from rest_framework.routers import DefaultRouter


urlpatterns = [
    url(r'uavs', UAVViewSet.as_view(), name="uavs")
]