from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from checkout.models import BillingAddress



class CheckoutForm(forms.ModelForm):


    country = CountryField(blank_label='(select country)').formfield(
        widget=CountrySelectWidget(attrs={

    }))
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Street name'
    }))
    city = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'City name'
    }))
    zip = forms.CharField()
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'phone number'
    }))
    email_address = forms.CharField()
    longitude = forms.CharField(max_length=50,required=True,widget= forms.HiddenInput)
    latitude = forms.CharField(max_length=50,required=True,widget= forms.HiddenInput)


    class Meta:
        model = BillingAddress
        fields = ('country','street_address','city','zip','phone','email_address','longitude','latitude')