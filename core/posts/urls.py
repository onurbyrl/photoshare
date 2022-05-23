from django.urls import path
from .views import PostList, PostCreate

app_name = 'posts'

urlpatterns = [
    path('', PostList.as_view(), name='postlist'),
    path('add/', PostCreate.as_view(), name='postcreate'),
]