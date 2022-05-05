from django.contrib import admin
from book.models import BlogPostmodel
# Register your models here.

class Blogpostadmin(admin.ModelAdmin):
    list_display=['author','title','body','createdat','updatedat']

admin.site.register(BlogPostmodel,Blogpostadmin)

