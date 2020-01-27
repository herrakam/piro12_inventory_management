from django import forms
from .models import Product,Client

class productform(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'