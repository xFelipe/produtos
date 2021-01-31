from django.forms import ModelForm
from product_manager.core.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'value', 'description']
