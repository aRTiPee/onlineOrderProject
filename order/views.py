from django.shortcuts import render
from .models import Menu, Customer, Order

<<<<<<< HEAD
# Create your views here.
def createUser(request):
=======
def home(request):
	return render(request, 'order/home.html')

def receipt(request):
	return render(request, 'order/receipt.html')
>>>>>>> 9d6ac85115d83386351d74b3cd606c61d044d30c
