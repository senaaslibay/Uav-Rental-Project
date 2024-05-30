
from rest_framework import views, status
from order.models import *
from rest_framework.response import Response
from order.serializers import *


class OrderViewSet(views.APIView):
    serializer_class = OrderSerializer

    def post(self, request, pk=None, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Added Successfully", status=status.HTTP_200_OK)
    
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            order = Orders.objects.get(id=pk)
            serializer = self.serializer_class(order)
            return Response(serializer.data, status=status.HTTP_200_OK)

        orders = Orders.objects.filter(user=request.data.user)
        serializer = self.serializer_class(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk=None, *args, **kwargs):
        if pk and pk.isdigit():
            order = Orders.objects.get(id=pk)
            serializer = self.serializer_class(order, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response("Updated Successfully", status=status.HTTP_200_OK)
        
    def delete(self, request, pk=None, *args, **kwargs):
        order=Orders.objects.get(id=pk)
        order.delete()
        return Response("Deleted Successfully", status=status.HTTP_200_OK)
