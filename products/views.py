from django.shortcuts import render

from products.models import Products

from django.http import JsonResponse

from products.forms import ProductFormModel

from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics

from products.serializer import Check_Serializer

# Create your views here.

class Generic_Api(generics.ListCreateAPIView):

    queryset = Products.objects.all()

    serializer_class = Check_Serializer