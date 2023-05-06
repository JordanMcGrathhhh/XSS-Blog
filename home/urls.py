from django.urls import path

from .views import Index, ReadPost, AddComment

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('posts/<str:post_id>', ReadPost.as_view(), name='read-post'),
    path('add-comment', AddComment.as_view(), name='add-comment')
]
