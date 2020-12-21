from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .filters import OrderFilter
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


def reg_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = SignUpForm()
    register=False
    if request.method == "POST":
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            register=True
            user=form.cleaned_data.get('username')
            messages.success(request,'Account created successfully for' + user)
            return redirect('login')
    context = {'form': form,'register':register}
    return render(request, 'accounts/registration.html', context)


def login_page(request):
    if request.method == 'POST':
       username= request.POST.get('username')
       password= request.POST.get('password')
       user = authenticate(request ,username=username,password=password)
       
       if user is not None: 
           login(request,user)
           return redirect('home')
       else:
           messages.info(request,"username OR password is incorrect")
    context = {}

    return render(request, 'accounts/login.html', context)

def logout_page(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_ordered = orders.count()

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='pending').count()

    context = {'orders': orders, 'customers': customers, 'total_ordered': total_ordered, 'delivered': delivered,
               'pending': pending}
    return render(request, 'accounts/dashbord.html', context)

@login_required(login_url='login')
def products(request):
    product = Product.objects.all()
    context = {'pd': product}
    return render(request, 'accounts/product.html', context)

@login_required(login_url='login')
def customer(request, pk):
    customers = Customer.objects.get(id=pk)
    orders = customers.order_set.all()
    orders_count = orders.count()
    my_filter = OrderFilter(request.GET, queryset=orders)
    orders = my_filter.qs
    context = {'customer': customers, 'order': orders, 'orders_count': orders_count, 'myFilter': my_filter}
    return render(request, 'accounts/customer.html', context)

@login_required(login_url='login')
def createOrder(request):
    forms = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': forms}
    return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}

    return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    # order.save()
    return redirect('/')
