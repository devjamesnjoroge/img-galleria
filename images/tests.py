from django.test import TestCase
from .models import Images

# Create your tests here.

class imagesTest(TestCase):
    def setUp(self):
        self.new_image = Images(image='image.jpg', name='image', description='image', location='image', category='image', date_taken='image')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image, Images))