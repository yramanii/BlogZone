from django.http import response
from django.test import TestCase
from django.test.client import Client
from django.test.testcases import SimpleTestCase
from django.urls.base import reverse

# view testing
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('index') 
        self.contact_url = reverse('contact')
        self.blog_url = reverse('create blog')
        self.signup_url = reverse('signup')
        self.login_url = reverse('login')

    def test_homepage(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    
    def test_contactpage(self):
        response = self.client.get(self.contact_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    
    def test_blogpage(self):
        response = self.client.get(self.blog_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'createblog.html')


    def test_signuppage(self):
        response = self.client.get(self.signup_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')


    def test_loginpage(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')


# Noraml Testing
class Test(SimpleTestCase):
    def test(self):
        assert 2==2
