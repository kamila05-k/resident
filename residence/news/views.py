from django.core.exceptions import ObjectDoesNotExist
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
from rest_framework.response import Response
from .models import Post, Status
from .serializers import PostSerializer, StatusSerializer
from django_filters.rest_framework import DjangoFilterBackend

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = None
    parser_classes = [MultiPartParser, FormParser]
    filter_backends = (DjangoFilterBackend,)
    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def get_object(self):
        slug = self.kwargs.get("slug")
        return Post.objects.get(slug=slug)

class StatusView(generics.ListAPIView):
    serializer_class = StatusSerializer
    filter_backends = [SearchFilter]
    search_fields = ['blog', 'post__title']
    def get(self, request, *args, **kwargs):
        try:
            model = Status.objects.all()
            serialized_status = self.serializer_class(model, many=True).data
            status_dict = {}
            for status in serialized_status:
                translated_blog_name = list(status.keys())[0]
                status_posts = status.pop(translated_blog_name)
                status_dict[translated_blog_name] = status_posts
            return Response(status_dict)
        except ObjectDoesNotExist:
            return Response({'error': 'Status is not found'}, status=status.HTTP_404_NOT_FOUND)
    def get_queryset(self):
        queryset = Status.objects.all()
        return queryset
