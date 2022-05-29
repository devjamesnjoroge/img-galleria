from django.db import models

# Create your models here.

class Images(models.Model):
    image = models.ImageField(upload_to='images/')
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
        self.update()

    def __str__(self):
        return self.name
