from products.models import Products

from rest_framework import generics

from products.serializer import ProductSerializer

class CreatAndShow(generics.ListCreateAPIView):

    queryset = Products.objects.all()

    serializer_class = ProductSerializer