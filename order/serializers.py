from rest_framework import serializers
from order.models import Customer, Order
from django.contrib.auth.models import User


class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = ('name', 'address', 'username')


class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = ('quantity_chicken', 'quantity_fries')