from django.contrib import admin
from .models import contact, createBlog

# Register your models here.
admin.site.register(contact)

admin.site.register(createBlog)


admin.site.site_header = "Blog-Zone Administration"

admin.site.site_title = "Administration"
# admin.site.register(login)

# admin.site.register(signup)
