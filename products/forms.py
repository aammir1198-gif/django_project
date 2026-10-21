from django.forms import ModelForm

from products.models import Products

class ProductFormModel(ModelForm):

    class Meta:

        model = Products

        fields = "__all__"