from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
import pyperclip


# Create your models here.

class Images(models.Model):
    image = CloudinaryField('images')
    name = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    date_taken = models.DateTimeField(auto_now_add=True)
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.objects.update()

    # Copy image to clipboard
    def copy_image(self):
        return pyperclip.copy(self.image.url)

    @classmethod
    def get_image(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_date(cls, date):
        image = cls.objects.filter(date_taken__date=date)
        return image

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.get(id = id)
        return image

    @classmethod
    def search_by_category(cls, search_term):
        images = cls.objects.filter(category__icontains=search_term)
        return images

    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(location__icontains=location)
        return images
    
    def __str__(self):
        return self.name
