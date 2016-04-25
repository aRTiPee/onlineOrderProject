from django import forms
from .models import Customer, Order
from django.forms import inlineformset_factory

class Sign(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ('name', 'address', 'username')

class Login(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ('username',)

class Buy(forms.ModelForm):
	class Meta:
		model = Order
		fields = ('quantity_chicken', 'quantity_fries', 'username')

class LogOut(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ('username',)

class Histori(forms.ModelForm):
	class Meta:
		model = Order
		fields = ('username',)