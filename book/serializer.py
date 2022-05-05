from rest_framework import serializers
from book.models import BlogPostmodel
class BlogPostserializer(serializers.ModelSerializer):
    class Meta:
        model=BlogPostmodel
        fields='__all__'


