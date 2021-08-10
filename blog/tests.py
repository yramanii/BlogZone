from django.test import TestCase
from .models import *

# Create your tests here.

class createBlogTest(TestCase):
    def setUp(self):
        createBlog.objects.create(title='the secret', author='Rhonda Byrne')

    def test(self):
        obj1 = createBlog.objects.get(title='the secret', author='Rhonda Byrne')
        self.assertEqual(obj1.title, 'the secret')
        self.assertEqual(obj1.author, 'Rhonda Byrne')

class contactTest(TestCase):
    def setUp(self) -> None:
        contact.objects.create(First_Name='yash', Last_Name='ramani', Email='yash@gmail.com')

    def test(self):
        obj2 = contact.objects.get(First_Name='yash', Last_Name='ramani', Email='yash@gmail.com')
        self.assertEqual(obj2.First_Name, 'yash')
        self.assertEqual(obj2.Last_Name, 'ramani')
        self.assertEqual(obj2.Email, 'yash@gmail.com')