from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from book import views
urlpatterns=[
    path('get_blog/',views.get_blogview.as_view(),name="get_blog"),
    path('blog/',views.blogview.as_view(),name="blog"),
    path('create_blog/',views.create_blogview.as_view(),name="create_blog"),
    path('update_blog/<int:pk>/',views.update_blogview.as_view(),name="update_blog"),

]

urlpatterns=format_suffix_patterns(urlpatterns)