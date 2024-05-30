
from rest_framework import views, status
from uavs.models import *
from rest_framework.response import Response
from uavs.serializers import *


class UAVViewSet(views.APIView):
    serializer_class = UAVSerializer

    def post(self, request, pk=None, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Added Successfully", status=status.HTTP_200_OK)
    
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            uav = UAVs.objects.get(id=pk)
            serializer = self.serializer_class(uav)
            return Response(serializer.data, status=status.HTTP_200_OK)

        uavs = UAVs.objects.filter(user=request.data.user)
        serializer = self.serializer_class(uavs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk=None, *args, **kwargs):
        if pk and pk.isdigit():
            uav = UAVs.objects.get(id=pk)
            serializer = self.serializer_class(uav, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response("Updated Successfully", status=status.HTTP_200_OK)
        
    def delete(self, request, pk=None, *args, **kwargs):
        uav=UAVs.objects.get(id=pk)
        uav.delete()
        return Response("Deleted Successfully", status=status.HTTP_200_OK)