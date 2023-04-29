from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget


class UserRegisterForm(UserCreationForm):
    FirstName = forms.CharField(max_length=255,required=True)
    LastName = forms.CharField(max_length=255,required=True)
    DOB = forms.DateField(widget=AdminDateWidget,help_text='Enter your birthdate')
    Phone = forms.IntegerField(required=True)
    email = forms.EmailField()
    Address = forms.CharField(max_length=255,required=True)
    City = forms.CharField(max_length=255,required=True)
    Country = forms.CharField(max_length=255,required=True)
    ZipCode = forms.CharField(max_length=255,required=True)
    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',
                  'FirstName', 'LastName', 'DOB', 'Phone', 'Address',
                   'City', 'Country', 'ZipCode']