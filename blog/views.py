from django.shortcuts import render
from .serializers import *

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import ProductSerializer
from .serializers import AboutSerialzer
from rest_framework.decorators import api_view  
from .serializers import PhoneNameSerializer







class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class AboutList(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerialzer

class PhoneNameCreateView(generics.CreateAPIView):
    queryset = PhoneName.objects.all()
    serializer_class = PhoneNameSerializer

class PortfolioList(APIView):
    def get(self, request):
        portfolios = Portfolio.objects.all()
        serializer = PortfolioSerializer(portfolios, many=True)
        return Response(serializer.data)
