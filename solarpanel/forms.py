from django import forms
from .models import *


class AddCustomerForm(forms.ModelForm):

    customer_name = forms.CharField(max_length=50, label='customer_name', widget=forms.TextInput(attrs={'placeholder': 'Customer Name','class':'form-control input-border-bottom rounded-0 p-0'}))
    customer_address = forms.CharField(max_length=50, label='customer_address', widget=forms.TextInput(attrs={'placeholder': 'Customer Address','class':'form-control input-border-bottom rounded-0 p-0'}))
    customer_phonenumber = forms.CharField(max_length=50, label='customer_phonenumber', widget=forms.TextInput(attrs={'placeholder': 'Customer Phone Number','class':'form-control input-border-bottom rounded-0 p-0'}))
    customer_zipcode = forms.CharField(max_length=50, label='customer_zipcode', widget=forms.TextInput(attrs={'placeholder': 'Customer zipcode','class':'form-control input-border-bottom rounded-0 p-0'}))

    class Meta:
        model = Customer
        fields = '__all__'
