from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        # fields = ("name", "img", "desc", "price", "offer", "end_date")
        labels = {
            'name': 'Product Name',
            'img': 'Product Image',
            'desc': 'Description',
            'price': 'Product Price',
            "offer": 'Product Special Offer',
            'end_date': 'Product End Date'

        }

        widgets = {
            'end_date': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }


