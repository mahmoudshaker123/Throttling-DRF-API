from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework.throttling import UserRateThrottle ,AnonRateThrottle

# Create your views here.

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    throttle_classes =[UserRateThrottle ,AnonRateThrottle]