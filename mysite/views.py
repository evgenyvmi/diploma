# This Python file uses the following encoding: utf-8
from django.shortcuts import render
from .models import Request
from .models import Client
from .models import Category
from .models import Product
from django.http import HttpResponseRedirect
#from .forms import RequestForm
from .forms import ClientCreationForm
from .forms import FullUserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'NIOKR/logout.html', {})
def post_list(request):
	a = False
	current_user = request.user
	if current_user.is_authenticated():
		client = Client.objects.filter(user = current_user).first()
		if client is not None:
			print 'client'
			a = True
	return render(request, 'NIOKR/Главная страница.html', {'client': a})
def post_login(request):
	if request.POST:
		auth_form = AuthenticationForm()
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = authenticate(username=username, password=password)
		print user
		if user is not None:
			print 'I am not wrong'
			login(request, user)
			return HttpResponseRedirect('http://127.0.0.1:8000/')
			#else:
		else:
			return render(request, 'NIOKR/index.html', {'form': auth_form})
	else: 
		auth_form = AuthenticationForm()
		return render(request, 'NIOKR/index.html', {'form': auth_form})
#def post_request(request):
#	return render(request, 'NIOKR/Заявка.html', {})

def create_request(request):
	# if this is a POST request we need to process the form data

	return render(request, 'NIOKR/Заявка.html', {})

def create_client(request):
	if request.method == 'POST':
		form1 = FullUserCreationForm(request.POST)
		form2 = ClientCreationForm(request.POST)
		if form1.is_valid():
			
			if form2.is_valid():
				u = form1.save()
				client = form2.save()
				client.user = u
				client.save(update_fields=['user'])
				return HttpResponseRedirect('http://127.0.0.1:8000/')
			else:
				return render(request, 'NIOKR/signup.html', {'form1': form1, 'form2': form2})			
		else:
			return render(request, 'NIOKR/signup.html', {'form1': form1, 'form2': form2})
	else:
		form1 = FullUserCreationForm()
        form2 = ClientCreationForm()
	return render(request, 'NIOKR/signup.html', {'form1': form1, 'form2': form2})

def catalogs(request):
	catalogs = Category.objects.all()
	products = Product.objects.all()
	return render(request, 'NIOKR/catalogs.html', {'catalogs': catalogs})

def cart(request):
	return render(request, 'NIOKR/cart.html', {})

def contacts(request):
	return render(request, 'NIOKR/contacts.html', {})