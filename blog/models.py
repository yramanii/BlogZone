from django.db import models
from django.db.models.signals import pre_save
from project2.utils import unique_slug_generator
# Create your models here.
class contact(models.Model):

    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Description = models.TextField()

    
    def __str__(self):
        return self.First_Name

class createBlog(models.Model):

    input = models.TextField()
    title = models.CharField(max_length=50)

    slug = models.SlugField(max_length=255, null=True, blank=True)

    author = models.CharField(max_length=20)
    image = models.ImageField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.title

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=createBlog)














# class login(models.Model):

#     username = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)

#     def __str__(self):
#         return self.username

# class signup(models.Model):

#     username = models.CharField(max_length=15)
#     email = models.EmailField()
#     password1 = models.CharField(max_length=100)
#     password2 = models.CharField(max_length=100)

#     def __str__(self):
#         return self.username
