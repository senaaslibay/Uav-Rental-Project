
from rest_framework import views, status, exceptions
from django.contrib.auth import authenticate
from dealer.models import *
from django.contrib import auth
from rest_framework.response import Response
from dealer.serializers import *

class AuthViewset(views.APIView):
    def post(self, request, pk=None, *args, **kwargs):
        if request.user.is_authenticated:
            return Response(request, 'customer/home_page.html')
        else:
            username = request.data['username']
            password = request.data['password']
            user = authenticate(request, username=username, password=password)
            try:
                customer = Customers.objects.get(user = user)
            except:
                raise exceptions.NotFound
            
            auth.login(request, user)
            return Response(customer, status=status.HTTP_200_OK)
                


class DealerViewset(views.APIView):
    serializer_class = DealerSerializer

    def post(self, request, pk=None, *args, **kwargs):
        try:
            user = User.objects.create_user(username = request.data.username, password = request.data.password, email = request.data.email)
            user.first_name = request.data.firstname
            user.last_name = request.data.lastname
            user.save()
        except:
            raise exceptions.ValidationError()
        
        try:
            area = Area.objects.get(city = request.data.city, pincode = request.data.pincode)
        except:
            area = Area(city = request.data.city, pincode = request.data.pincode)
            area.save()
            area = Area.objects.get(city = request.data.city, pincode = request.data.pincode)

        dealer_data = {"user": user, "mobile":request.data.mobile, "area":area}
        serializer = self.serializer_class(data=dealer_data, context={'request': request}) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data)
        

    def get(self, request, pk=None, *args, **kwargs):
        if not pk.isdigit():
            raise exceptions.NotFound
        instance = Customers.objects.filter(pk=pk).first()
        if not instance:
            raise exceptions.NotFound
        return Response(instance, status=status.HTTP_200_OK)
