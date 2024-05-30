from django.urls import re_path as url
from order.views import *


urlpatterns = [
    url(r'rent/', OrderViewSet.as_view(), name="rent")
]