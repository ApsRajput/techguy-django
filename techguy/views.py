from django.shortcuts import render
from techguy.models import Techguy

# Create your views here.

def index(request):
    blogs = Techguy.objects.all()
    context = {'blogs' : blogs}
    return render(request, 'index.html', context)

def detail(request, pk):
    blog = Techguy.objects.get(pk=pk)
    context={'blog' : blog}
    return render(request, 'detail.html', context)