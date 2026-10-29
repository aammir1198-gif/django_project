from rest_framework import serializers

from products.models import Products

class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Products

        fields = ['name' , 'price' , 'count' , 'desciption' , 'category']

    def to_internal_value(self, data):

        supercall = super().to_internal_value(data)

        if supercall['desciption'] == None:

            supercall['desciption'] = 'some'

        return supercall