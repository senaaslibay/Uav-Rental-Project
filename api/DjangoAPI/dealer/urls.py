from django.conf.urls import include
from django.urls import re_path as url
from dealer.views import *
from rest_framework.routers import DefaultRouter


urlpatterns = [
    url(r'login', AuthViewset.as_view(), name="login"),
    url(r'register', DealerViewset.as_view(), name="register"),
]