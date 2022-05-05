from re import U
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class BlogPostmodel(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.TextField()
    body=models.TextField()
    createdat=models.DateTimeField(auto_now_add=True)
    updatedat=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
