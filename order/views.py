from django.shortcuts import render, get_object_or_404
from .models import Customer, Order
from .forms import Sign, Login, Buy
import sys
from pprint import pprint

def home(request):
	if request.method == "POST":
		form = Sign(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			name =	post.name
			address = post.address
			username = post.username
			post.save()
			return render(request, 'order/sign-up.html', {'name': name, 'address':address, 'username':username})

def menu(request):
	if request.method == "POST":
		form = Login(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			username = post.username
			l = get_object_or_404(Customer, username=username)
			#l = Customer.objects.get(username=username)
			if l:
				l.is_login = True
				l.save()
				return render(request, 'order/home.html', {'username': username})

def receipt(request):
	if request.method == "POST":
		form = Buy(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			username = post.username
			quantity_chicken = post.quantity_chicken
			quantity_fries = post.quantity_fries
			total = quantity_chicken * 250 + quantity_fries * 100
			post.cost = total
			post.save()
		return render(request, 'order/receipt.html', {'username':username, 'quantity_chicken':quantity_chicken, 'quantity_fries':quantity_fries, 'total':total})

def sign(request):
	return render(request, 'order/sign-up.html')

def sign1(request):
 	return render(request, 'order/sign.html')