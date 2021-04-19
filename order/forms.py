from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

class OrderForm(ModelForm):
	OPTIONS= (
		('Postpay','Postpay'),
		('Prepay (Full)','Prepay (Full)'),
		('Prepay (Half)', 'Prepay (Half)')
	)
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)
	payment_option = forms.TypedChoiceField(required=True, choices=OPTIONS, widget=forms.RadioSelect(attrs={'class':'form-check-inline'}))
	customer_name =  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'text'}))
	address =  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'text'}))
	phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'text'}))
	product_name = forms.ModelChoiceField(queryset=Product.objects.all(),widget=forms.Select(attrs={'class':'form-control','placeholder':'Select a product'}))
	status = forms.ChoiceField(choices=STATUS,widget=forms.Select(attrs={'class':'form-control','placeholder':'Select status'}))

	class Meta:
		model = Order
		fields = '__all__'

class UserRegisterForm(UserCreationForm):
   email = forms.EmailField()

   class Meta:
	   model = User
	   fields = ['username','email','password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	class Meta:
		model= User
		fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model= Profile
		fields=['name','image']

class ChangePasswordForm(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
	new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
	new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))

	class Meta:
		model= User
		fields =['old_password','new_password1','new_password2']

