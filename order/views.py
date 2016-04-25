from django.shortcuts import render, get_object_or_404
from django.http import Http404
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

def receipt(request, getusername):
	pprint("hello")
	if request.method == "POST":
		pprint("hello2")
		form = Buy(request.POST)
		if form.is_valid():
			pprint("after is_valid")
			post = form.save(commit=False)
			username = getusername
			quantity_chicken = post.quantity_chicken
			quantity_fries = post.quantity_fries
			pprint(post.username + "user")
			pprint(post.quantity_chicken + "chick")
			pprint(post.quantity_fries + "fris")
			post.save()
		else: raise Http404
		return render(request, 'order/receipt.html', {
			'username': getusername,})

def sign(request):
	return render(request, 'order/sign-up.html')

def sign1(request):
 	return render(request, 'order/sign.html')