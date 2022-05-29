from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Images

# Create your views here.

def index(request):
    images = Images.get_image()
    return render(request, 'index.html', {"images": images})

