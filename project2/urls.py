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
import django
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from blog import views
from blog.views import HomePageView, createBlog, LoginView, signupView, contact

from django.conf import settings
from django.views.static import serve
from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='index'),
    path('contact/', contact.as_view(), name='contact'),
    path('createblog/', createBlog.as_view(), name='create blog'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', signupView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += [
#         url(r'^media/(?P<path>.*)$', serve, {
#             'document_root':settings.MEDIA_ROOT,
#         }),
#     ]