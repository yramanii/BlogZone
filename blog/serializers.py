from venv import create
from rest_framework.serializers import HyperlinkedModelSerializer

from blog.models import createBlog

class blogPostSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = createBlog
        fields = ['input', 'title', 'author', 'image', 'file']