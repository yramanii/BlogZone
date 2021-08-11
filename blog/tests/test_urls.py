from django.test import TestCase
from blog.views import *
from django.urls import resolve, reverse

class test(TestCase):

    def test_index(self):
        url = reverse('index')
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, HomePageView)

    def test_contact(self):
        url = reverse('contact')
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, contact)

    def test_blog(self):
        url = reverse('create blog')
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, createBlog)

    # def test_login(self):
    #     url = reverse('login')
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_signup(self):
        url = reverse('signup')
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, signupView)