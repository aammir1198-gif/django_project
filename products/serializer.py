from rest_framework import serializers

from products.models import Products

class Check_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Products

        fields = '__all__'