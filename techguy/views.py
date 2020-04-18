from django.shortcuts import render
from techguy.models import Techguy, Category
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import ContactForm
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

# Create your views here.

# class TechguyListView(ListView):
#     model = Techguy
#     template_name = 'index.html'
#     context_object_name = 'blogs'

def TechguyListView(request):
    blogs = Techguy.objects.all()
    data = {"results": 
        list(blogs.values(
            "title",
            "description",
            "slug",
            "technology"))
            }
    return JsonResponse(data)

    data = { "results" : {
        "title" : blogs.title,
        "description" : blogs.description,
        "slug" : blogs.slug,
        "technology" : blogs.technology,
        }
    }

# class TechguyDetailView(DetailView):
#     model = Techguy
#     template_name = 'detail.html'
#     context_object_name = 'blog'
#     slug_url_kwarg = 'slug'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category'] = Category.objects.all()
#         return context

def TechguyDetailView(request, pk):
    techguy = get_object_or_404(Techguy, pk=pk)
    data = { "results" : {
        "title" : techguy.title,
        "description" : techguy.description,
        "slug" : techguy.slug,
        "technology" : techguy.technology,
        }
    }
    return JsonResponse(data)

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