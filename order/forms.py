from django import forms
from .models import Customer, Order

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
