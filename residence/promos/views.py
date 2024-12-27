from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Banner
from .serializers import BannerSerializer


class BannerView(APIView):

    def get(self, request, *args, **kwargs):
        """
        Получить список всех баннеров.
        """
        banners = Banner.objects.all()
        serializer = BannerSerializer(banners, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)