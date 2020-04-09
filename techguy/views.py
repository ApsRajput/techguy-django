from django.shortcuts import render
from techguy.models import Techguy
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm

# Create your views here.

def index(request):
    blogs = Techguy.objects.all()
    context = {'blogs' : blogs}
    return render(request, 'index.html', context)

def detail(request, pk):
    blog = Techguy.objects.get(pk=pk)
    context={'blog' : blog}
    return render(request, 'detail.html', context)

# def mail(request):
    # # subject = request.POST.get('subject', '')
    # # message = request.POST.get('message', '')
    # # from_email = request.POST.get('from_email', '')

    # subject = 'django function mail'
    # message = 'django function mail success'
    # from_email = 'webshot.tech@gmail.com'
    # if subject and message and from_email:
    #     try:
    #         send_mail(subject, message, from_email, ['apsrajput008@gmail.com'])
    #     except BadHeaderError:
    #         return HttpResponse('Invalid header found.')
    #     return HttpResponseRedirect('/techguy/')
    # else:
    #     # In reality we'd use a form class
    #     # to get proper validation errors.
    #     return HttpResponse('Make sure all fields are entered and valid.')

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