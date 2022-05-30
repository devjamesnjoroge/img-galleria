from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^images/$', views.images, name='images'),
    path('image/<int:id>', views.image, name='image'),
    path('copy_image_url/<int:id>', views.copy_image_url, name='copy_image_url'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)