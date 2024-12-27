from django.urls import path
from .views import BannerView

urlpatterns = [
    path('banners/', BannerView.as_view(), name='banner-list-create'),
]
