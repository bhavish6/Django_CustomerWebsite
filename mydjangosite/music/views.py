from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
#create your views here
from .models import *
from .forms import orderForm,CreateUserForm
from .filters import *
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import *

@unauthenticated_user
def registerPage(request):


    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='Userss')
            user.groups.add(group)
            messages.success(request,'The account was created for '+ username)
            return redirect('login')


    context ={'form':form}
    return render(request, 'music/register.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is incorrect ')

    context ={}
    return render(request, 'music/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')





@login_required(login_url='login')
@admin_only
def home(request):
    Orders = order.objects.all()
    Customers = Customer.objects.all()
    total_customers = Customers.count()
    total_orders = Orders.count()
    delivered = Orders.filter(status='Delivered').count()
    pending = Orders.filter(status='Pending').count()

    context ={'Customers':Customers , 'Orders':Orders ,'total_customers':total_customers ,'total_orders': total_orders,'delivered': delivered ,'pending':pending }      #The key in the dictionary needs to be passed in the html template for loop

    return render(request , 'music/dashboard.html' , context)


@login_required(login_url='login')

def userPage(request):


    context={}

    return render(request , 'music/user.html' , context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Adminn'])
def products(request):
    products = product.objects.all()
    return render(request , "music/products.html" , {'products':products})


@login_required(login_url='login')
@allowed_users(allowed_roles=['Adminn'])
def getcustomer(request, pk):
    cust = Customer.objects.get(id=pk)    #accesses the database
    orders = cust.order_set.all()   #quering customers child object from models field,in set id always use lowercase
    order_count = orders.count()

    myFilter = OrderFilter(request.GET , queryset=orders)
    orders = myFilter.qs
    context =  {'cust':cust ,'orders':orders ,'order_count':order_count ,'myFilter':myFilter}
    return render(request , "music/Customer.html" ,context)


@login_required(login_url='login')
def createorder(request,pk):
    orderFormSet = inlineformset_factory(Customer , order ,fields=('Product','status'),extra=2)
    getord = Customer.objects.get(id=pk)
    formset = orderFormSet(queryset=order.objects.none(),instance = getord)
    # form = orderForm()
    if request.method == 'POST':
       # print("printing post:",request.POST)
       # form = orderForm(request.POST)
        formset = orderFormSet(request.POST,instance=getord)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context={'formset':formset}
    return render(request , "music/order_form.html" ,context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Adminn'])
def updateorder(request, pkey):     #the user data is prefiled in this so we can update it
    getorder = order.objects.get(id=pkey)
    form = orderForm(instance=getorder)
    if request.method == 'POST':
        form = orderForm(request.POST,instance=getorder)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, "music/order_form.html", context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Adminn'])
def deleteorder(request, pk):
    item = order.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context={'item':item}
    return render(request, "music/delete.html", context)

