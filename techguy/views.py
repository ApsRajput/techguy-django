from django.shortcuts import render
from techguy.models import Techguy, Category
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.views.generic import ListView, DetailView

# Create your views here.

class TechguyListView(ListView):
    model = Techguy
    template_name = 'index.html'
    context_object_name = 'blogs'

class TechguyDetailView(DetailView):
    model = Techguy
    template_name = 'detail.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

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