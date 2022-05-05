from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,ListAPIView,CreateAPIView,UpdateAPIView,RetrieveUpdateDestroyAPIView
from book.serializer import BlogPostserializer
from book.models import BlogPostmodel
from book.pagination import BlogPostpegination
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.
class get_blogview(ListAPIView):
    serializer_class=BlogPostserializer
    queryset=BlogPostmodel.objects.all()
    pagination_class=BlogPostpegination
    permission_classes = (IsAuthenticated, )

class create_blogview(CreateAPIView):
    serializer_class=BlogPostserializer
    permission_classes = (IsAuthenticated, )

class blogview(ListCreateAPIView):
    serializer_class=BlogPostserializer
    queryset=BlogPostmodel.objects.all()
    permission_classes = (IsAuthenticated, )

class update_blogview(UpdateAPIView):
    serializer_class=BlogPostserializer
    queryset=BlogPostmodel.objects.all()
    permission_classes = (IsAuthenticated, )

class update_blogview(RetrieveUpdateDestroyAPIView):
    serializer_class=BlogPostserializer
    queryset=BlogPostmodel.objects.all()
    permission_classes = (IsAuthenticated, )

    