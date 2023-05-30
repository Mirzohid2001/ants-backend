from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name','price','image','size','description')



class AboutSerialzer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('title','about','cost')

class PhoneNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneName
        fields = ['id', 'name', 'phone']


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'
