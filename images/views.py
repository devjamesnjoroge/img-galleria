from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Images

# Create your views here.

def index(request):
    return render(request, 'index.html')

def images(request):
    images = Images.get_image()
    return render(request, 'images.html', {"images": images})

def search_results(request):
    if 'Image' in request.GET and request.GET["Image"]:
        search_term = request.GET.get("Image")
        searched_images = Images.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})