from django.shortcuts import render, redirect
from techguy.models import *
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm, TechguyForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

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

def customers(request):
    customers = Customer.objects.all()
    context = {
        "customers" : customers
    }
    return render(request, 'order/customers.html', context)

def products(request):
    products = Product.objects.all()
    context = {
        "products" : products
    }
    return render(request, 'order/products.html', context)

def orders(request):
    orders = Order.objects.all()
    context = {
        "orders" : orders
    }
    return render(request, 'order/orders.html', context)