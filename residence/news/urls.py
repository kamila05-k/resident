from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),  # Список постов
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('status', StatusView.as_view(), name='status'),
]
