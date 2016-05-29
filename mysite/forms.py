# This Python file uses the following encoding: utf-8
from django.forms import ModelForm
from .models import Order_product
from .models import Order
from .models import Client
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
"""

class RequestForm(ModelForm):
	class Meta: 
		model = Request
		fields = ['research_interests', 'title', 'description']

#class FullUserCreationForm(ModelForm):
#	class Meta:
#		model = User
#		fields = ['username', 'password', 'first_name', 'last_name', 'email']

#class FullUserCreationForm(ModelForm):
#	class Meta:
#		model = User
#		fields = ['first_name', 'last_name', 'email']

"""	
class FullUserCreationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(FullUserCreationForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		user.first_name = self.cleaned_data["first_name"]
		user.last_name = self.cleaned_data["last_name"]
		if commit:
			user.save()
		return user

class ClientCreationForm(ModelForm):
	class Meta:
		model = Client
		fields = ("organization", "position", "phone_number", "address")

class AddProductForm(ModelForm):
	class Meta:
		model = Order_product
		fields = ('quantity',)

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = ('is_temporary',)