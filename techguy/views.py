from django.shortcuts import render, redirect
from techguy.models import Techguy, Category
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm, TechguyForm
from django.views.generic import ListView, DetailView

# Create your views here.

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
    if request.method == "Post":
        form = TechguyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/index.html')
            except:
                pass
    else:
        form = TechguyForm()
    return render(request, 'create.html', {'form':form})

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
        return redirect("/index")  
    return render(request, 'edit.html', {'techguy': techguy})

def destroy(request, id):  
    techguy = Techguy.objects.get(id=id)  
    techguy.delete()  
    return redirect("/index.html")  

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