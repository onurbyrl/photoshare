from django.urls import path
from api.views import PostList, PostCreate

# app_name

urlpatterns = [
    path('', PostList.as_view(), name='postlist'),
    path('create/', PostCreate.as_view(), name='postcreate'),
]