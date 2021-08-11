from django.test import TestCase
from blog.models import *

# Create your tests here.

# Model Testing
class createBlogTest(TestCase):
    def setUp(self):
        createBlog.objects.create(title='the secret', author='Rhonda Byrne')
        # contact.objects.create(First_Name='yash', Last_Name='ramani', Email='yash@gmail.com')

    def test1(self):
        obj1 = createBlog.objects.get(title='the secret', author='Rhonda Byrne')
        self.assertEqual(obj1.title, 'the secret')
        self.assertEqual(obj1.author, 'Rhonda Byrne')

    # def test2(self):
    #     obj2 = contact.objects.get(First_Name='yash', Last_Name='ramani', Email='yash@gmail.com')
    #     self.assertEqual(obj2.First_Name, 'yash')
    #     self.assertEqual(obj2.Last_Name, 'ramani')
    #     self.assertEqual(obj2.Email, 'yash@gmail.com')

class contactTest(TestCase):
    def setUp(self):
        contact.objects.create(First_Name='yash', Last_Name='ramani', Email='yash@gmail.com')

    def test(self):
        obj2 = contact.objects.get(First_Name='yash', Last_Name='ramani', Email='yash@gmail.com')
        self.assertEqual(obj2.First_Name, 'yash')
        self.assertEqual(obj2.Last_Name, 'ramani')
        self.assertEqual(obj2.Email, 'yash@gmail.com')