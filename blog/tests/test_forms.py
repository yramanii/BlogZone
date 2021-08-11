from django.test import SimpleTestCase, TestCase
from blog.forms import *

class formTest(SimpleTestCase):

    def test_contactform(self):
        form1 = contactForm(data={
            'First_Name': 'yash',
            'Last_Name': 'ramani',
            'Email': 'yash@gmail.com',
            'Description': 'Hi'
        })

        self.assertTrue(form1.is_valid())

    def test_blogform(self):
        form2 = blogForm(data={
            'input': 'hi there',
            'author': 'yash',
            'title': 'testing',
            'image': '',
            'file': '',
        })

        self.assertTrue(form2.is_valid())

class signup(TestCase):

    def test_signupform(self):
        form3 = signupForm(data={
            'username': 'yash',
            'email': 'yash@gmail.com',
            'password1': 'yash1',
            'password2': 'yash1'
        })

        self.assertFalse(form3.is_valid())