from rest_framework import serializers
from dealer.models import *

class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealers
        exclude = ()