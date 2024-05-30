from rest_framework import serializers
from uavs.models import *

class UAVSerializer(serializers.ModelSerializer):
    class Meta:
        model = UAVs
        fields = '__all__'