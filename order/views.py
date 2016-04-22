from django.shortcuts import render
from .models import Customer, Order


def home(request):
	return render(request, 'order/home.html')

def receipt(request):
	return render(request, 'order/receipt.html')