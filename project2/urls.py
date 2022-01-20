"""project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template import base
from django.urls import path, include
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url
from django.conf.urls.static import static
 
from blog.views import HomePageView, CreateBlog, LoginView, signupView, contact, details, blogApiView

from rest_framework import routers

router = routers.DefaultRouter()
router.register('blog-post', blogApiView, basename='blogapi')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomePageView.as_view(), name='index'),
    path('contact/', contact.as_view(), name='contact'),
    path('createblog/', CreateBlog.as_view(), name='create blog'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', signupView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('post/<slug:slug_text>', details),

    path('api/', include(router.urls)),
    path('api-auth/', include("rest_framework.urls")),

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += [
#         url(r'^media/(?P<path>.*)$', serve, {
#             'document_root':settings.MEDIA_ROOT,
#         }),
#     ]