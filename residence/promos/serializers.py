from rest_framework import serializers
from .models import Banner

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id', 'blog', 'ratation', 'pc_image', 'mb_img', 'url', 'date']
