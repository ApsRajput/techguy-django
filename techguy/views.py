from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from django.forms import formset_factory
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .filters import *
from .decorators import *

@unauthenticated_user
def register(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')

    context = {'form':form}
    return render(request, 'registration/register.html', context)

#View Caching
# from django.views.decorators.cache import cache_page

# Create your views here.
#Auth
# class MyView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = 'redirect_to'
#Generic Classes
# class TechguyListView(ListView):
#     model = Techguy
#     template_name = 'index.html'
#     context_object_name = 'blogs'

# class TechguyDetailView(DetailView):
#     model = Techguy
#     template_name = 'detail.html'
#     context_object_name = 'blog'
#     slug_url_kwarg = 'slug'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category'] = Category.objects.all()
#         return context

#Simple Crud Operations
def create(request):
    if request.method == "POST":
        form = TechguyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TechguyForm()
    return render(request, 'create.html', {'form':form})

# cache_page(200)
@login_required
def show(request):
    techguy = Techguy.objects.all()
    return render(request, 'index.html', {'techguy':techguy})

def edit(request, id):  
    techguy = Techguy.objects.get(id=id)  
    return render(request,'edit.html', {'techguy':techguy})

def update(request, id):  
    techguy = Techguy.objects.get(id=id)
    form = TechguyForm(request.POST, instance = techguy)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'edit.html', {'techguy': techguy})

def destroy(request, id):  
    techguy = Techguy.objects.get(id=id)  
    techguy.delete()  
    return redirect("/")  

def mail(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['apsrajput008@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/techguy/mail/')
    return render(request, "contact.html", {'form': form})

class ContactForm(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/techguy/mail/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

# using cookie
def showcookie(request):
    show = request.COOKIES['webshot']
    visit = request.COOKIES['visits']
    html = "<center> New Page <br>{0}</center>".format(show)
    return HttpResponse(html)

# user visit
def visitcookie(request):
    html = HttpResponse("<h1>WebShot Django Tutorial</h1>")
    if request.COOKIES.get('visits'):
        html.set_cookie('webshot', 'Welcome Back')
        value = int(request.COOKIES.get('visits'))
        html.set_cookie('visits', value + 1)
    else:
        value = 1
        text = "Welcome for the first time"
        html.set_cookie('visits', value)
        html.set_cookie('webshot', text)
    return html

def deletecookie(request):
    if request.COOKIES.get('visits'):
       response = HttpResponse("<h1>Webshot<br>Cookie deleted</h1>")
       response.delete_cookie("visits")
    else:
        response = HttpResponse("<h1>Webshot</h1>need to create cookie before deleting")
    return response

# Sessions
def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>Webshot<br> the session is set</h1>")

def access_session(request):
    response = "<h1>Welcome to Sessions of Webshot</h1><br>"
    if request.session.get('name'):
        response += "Name : {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(request.session.get('password'))
        return HttpResponse(response)
    else:
        return redirect('create/')

def index(request):
    return render(request, 'order/index.html')

@admin_only
def customers(request):
    customers = Customer.objects.all()

    context = {
        "customers" : customers,
    }
    return render(request, 'order/customers.html', context)

def customer_detail(request, pk):
    customer = Customer.objects.get(pk=pk)
    orders = Order.objects.filter(customer__name=customer)
    context = {
        "customer" : customer,
        "orders" : orders
    }
    return render(request, 'order/customerdetail.html', context)

def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')
        else:
            return HttpResponse('Error in fields')
    else:
        form = CustomerForm()
        context = {
            'form' : form
        }
    return render(request, 'order/createform.html', context)
    
def update_customer(request, id):
    customer = Customer.objects.get(id=id)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers')
        else:
            return HttpResponse('Error in fields')

    form = CustomerForm(instance=customer)
    context = {
        'form' : form
    }
    return render(request, 'order/updateform.html', context)


def delete_customer(request, id):
    customer = Customer.objects.get(id=id)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        customer.delete()
        return redirect('customers')

    else:
        context = {
            'customer' : customer
        }
    return render(request, 'order/deletecustomer.html', context)

# Product Operations
def products(request):
    products = Product.objects.all()
    myFilter = ProductFilter(request.GET, queryset=Product.objects.all())
    
    context = {
        "products" : products,
        "myFilter" : myFilter
    }
    return render(request, 'order/products.html', context)

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        "product" : product
    }
    return render(request, 'order/productdetail.html', context)

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            return HttpResponse('Error in fields')
    else:
        form = formset_factory(ProductForm, min_num=1, validate_min=True)
        context = {
            'form' : form
        }
    return render(request, 'order/createform.html', context)
    
def update_product(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            return HttpResponse('Error in fields')

    form = ProductForm(instance=product)
    context = {
        'form' : form
    }

    return render(request, 'order/updateform.html', context)

def delete_product(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        product.delete()
        return redirect('products')

    else:
        context = {
            'product' : product
        }
    return render(request, 'order/deleteproduct.html', context)

# Generic View
class ListOrder(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'order/orders.html'

class DetailOrder(DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'order/orderdetail.html'

class CreateOrder(CreateView):
    model = Order
    fields = '__all__'
    context_object_name = 'form'
    template_name = 'order/createform.html'

class UpdateOrder(UpdateView):
    model = Order
    fields = '__all__'
    context_object_name = 'form'
    template_name = 'order/updateform.html'
    success_url = reverse_lazy('orders')

class DeleteOrder(DeleteView):
    model = Order
    success_url = reverse_lazy('orders')
    template_name = 'order/deleteorder.html'

# def delete_order(request, id):
#     order = Order.objects.get(id=id)

#     if request.method == 'POST':
#         form = OrderForm(request.POST, instance=order)
#         order.delete()
#         return redirect('products')

#     else:
#         context = {
#             'order' : order
#         }
#     return render(request, 'order/deleteorder.html', context)