# This Python file uses the following encoding: utf-8
from django.shortcuts import render
from simple_search import generic_search, perform_search

from .models import Order
from .models import Client
from .models import Category
from .models import Product
from .models import Order_product
from django.http import HttpResponseRedirect
#from .forms import RequestForm
from .forms import ClientCreationForm
from .forms import FullUserCreationForm
from .forms import AddProductForm
from .forms import OrderForm
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
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
	print request.GET
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
				data = {'is_temporary': True}
				print request.POST
				print data
				order = OrderForm(data)
				if order.is_valid():
					cart = order.save()
					cart.client = client
					cart.save(update_fields=['client'])
				else:
					print 'WTF???'

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
	current_client= Client.objects.filter(user=request.user)
	order = Order.objects.filter(client=current_client, is_temporary=True)
	products_in_order = Order_product.objects.filter(order=order)
	if len(products_in_order)==0:
		warning='Ваша корзина пока пуста'
		return render(request, 'NIOKR/cart.html', {'orders': order, 'warning': warning})
	else:
		return render(request, 'NIOKR/cart.html', {'orders': order, 'products_in_order': products_in_order})

def contacts(request):
	return render(request, 'NIOKR/contacts.html', {})

def products(request, category):
	products = Product.objects.filter(category= category)
	print products
	return render(request, 'NIOKR/products.html', {'products': products})

def product(request, category, slug):
	product = Product.objects.get(slug= slug)
	if request.method == 'POST':
		form = AddProductForm(request.POST)
		current_client= Client.objects.filter(user=request.user)
		order = Order.objects.get(client=current_client, is_temporary=True)
		if form.is_valid():
			order_product= form.save()
			order_product.order = order
			order_product.product= product
			order_product.save(update_fields=['order', 'product'])
	else:
		form = AddProductForm()
	return render(request, 'NIOKR/product.html', {'product': product, 'category': category, 'slug': slug, 'form': form})

class DeleteProductFromCart(DeleteView):
	model = Order_product
	success_url = reverse_lazy('order_product-list')

QUERY = "search-query"

MODEL_MAP = {
	Product: ["name", "category__name"]
}

def search(request):
	objects = []
	for model, fields in MODEL_MAP.iteritems():
		objects += generic_search(request, model, fields)
		print request.GET.get('q', "")
	return render(request, "NIOKR/search_results.html", {"objects": objects,"search_string": request.GET.get('q', ""),})