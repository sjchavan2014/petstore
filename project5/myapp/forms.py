from django import forms
from.models import Django_sagar,Address
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class django_form(forms.ModelForm):
    gen = (('male','male'),('female','female'),('other','other'))
    gender = forms.ChoiceField(choices=gen,widget=forms.RadioSelect)

    ct =(('Mumbai','Mumbai'),('Thane','Thane'),('Ghatkoper','Ghatkoper'),('Nashik','Nashik'))
    city = forms.ChoiceField(choices=ct,widget=forms.Select)
    class Meta:
        model = Django_sagar
        fields = '__all__'

class Signup_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

    
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'