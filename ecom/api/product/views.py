from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all().order_by('product_id')
    serializer_class=ProductSerializer


