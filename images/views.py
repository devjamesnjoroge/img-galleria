from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Images
import pyperclip

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

def image(request, id):
    try:
        image = Images.get_image_by_id(id)
    except:
        raise Http404()
    return render(request, 'image.html', {"image": image})

def copy_image_url(request, id):
    image = Images.get_image_by_id(id)
    image.copy_image()
    message = "Image URL Copied"
    return render(request, 'image.html', {"image": image, "message": message})

    
    