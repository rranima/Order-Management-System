from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from .forms import OrderForm, UserRegisterForm,UserUpdateForm, ProfileUpdateForm, ChangePasswordForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def registeruser(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form=UserRegisterForm()
		if request.method=='POST':
			form=UserRegisterForm(request.POST)
			try:
				if form.is_valid:
					form.save()
					username = form.cleaned_data.get('username')
					messages.success(request, f'Account created for {username}!')
					return redirect('login')
			except ValueError:
				messages.info(request, '')
		return render(request,'order/register.html',{'form':form})


def loginuser(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username=request.POST.get('username')		
			password=request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')
		context = {}
		return render(request, 'order/login.html', context)


def logoutuser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def userprofile(request):
	u_form = UserUpdateForm(instance=request.user)
	p_form = ProfileUpdateForm(instance=request.user.profile)
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST,instance=request.user)
		p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()

	context={'u_form':u_form,'p_form':p_form}
	return render(request,'order/account.html',context)


class ChangePassword(LoginRequiredMixin,PasswordChangeView):
	form_class=ChangePasswordForm
	success_url = reverse_lazy('profile')

def checkhome(request):
	return render(request, 'order/dash.html')

@login_required(login_url='login')
def home(request):
	orders = Order.objects.all()
	products = Product.objects.all()
	if ('q' in request.GET) and request.GET['q']:
			query_string= request.GET.get('q')
			orders= Order.objects.filter(Q(customer_name__icontains = query_string)|
										Q(product_name__name__icontains = query_string)|
										Q(status__icontains = query_string) )
				
	#	else:
	#		orders = None
	return render(request,'order/homepage.html',{'orders':orders,'products':products})

@login_required(login_url='login')
def products(request):
	products= Product.objects.all()
	return render(request,'order/products.html',{'products':products})

@login_required(login_url='login')
def createOrder(request):
	form = OrderForm()
	if request.method =='POST':
		form= OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')	
		else:
			print('invalid form')
			print(form.errors)

	context={'form':form}
	return render(request, 'order/neworder.html',context)

@login_required(login_url='login')
def updateOrder(request,pk):
	order= Order.objects.get(id=pk)
	form = OrderForm(instance=order)
	if request.method =='POST':
		form= OrderForm(request.POST,instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')
		
	context={'form':form}
	return render(request, 'order/neworder.html',context)

@login_required(login_url='login')
def deleteOrder(request,pk):
	order= Order.objects.get(id=pk)
	if request.method =='POST':
		order.delete()
		return redirect('/')

	context={'item': order}
	return render(request, 'order/deleteorder.html',context)

@login_required(login_url='login')
def search(request):
	orders = Order.objects.all()
	products = Product.objects.all()
	if ('q' in request.GET) and request.GET['q']:
		query_string= request.GET.get('q')
		orders= Order.objects.filter(Q(customer_name__icontains = query_string)|
									Q(product_name__name__icontains = query_string)|
									Q(status__icontains = query_string) )
			
#	else:
#		orders = None
	return render(request,'order/homepage.html',{'orders':orders,'products':products})

#def customer(request):
#	customer= Customer.objects.get(id=pk_test)
#	orders= Customer.order_set.all()

#	order_count= orders.count()	
#	context={'customer':customer}
#	return render(request,'order/customer.html',{'customer': customer})
