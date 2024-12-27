from rest_framework import serializers
from .models import *

class PostSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostSlider
        fields = [
            'image'
        ]

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostDetail
        fields = [
            'description'
        ]

class PostFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostFile
        fields = [
            'title', 'file'
        ]

class CommentSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Comments
        fields = ['post', 'user', 'comment', 'date', 'is_active']
    def create(self, validated_data):
        return Comments.objects.create(**validated_data)
    def get_date(self, obj):
        if obj.created_at:
            return obj.created_at.strftime('%Y-%m-%d')

class PostSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, source='comments', read_only=True)
    detail = PostDetailSerializer(many=True, read_only=True)
    slider = PostSliderSerializer(many=True, read_only=True)
    exception = PostFileSerializer(many=True, read_only=True)
    cat_title = serializers.SerializerMethodField()
    sub_cat_title = serializers.SerializerMethodField()
    views = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format='%H:%M %d.%m.%Y')
    updated_at = serializers.DateTimeField(format='%H:%M %d.%m.%Y')
    user = serializers.SerializerMethodField()
    def get_user(self, obj):
        if obj.user:
            return f'{obj.user.last_name} {obj.user.first_name}'
        return None
    def get_cat_title(self, obj):
        return obj.cat.title if obj.cat else "Категория не указана"
    def get_sub_cat_title(self, obj):
        return obj.sub_cat.title if obj.sub_cat else "Подкатегория не указана"
    def get_views(self, obj):
        return obj.views if obj.views is not None else 0
    class Meta:
        model = Post
        fields = [
            'id', 'user', 'slug', 'cat_title', 'sub_cat_title',
            'title', 'img', 'tags', 'is_active', 'created_at',
            'updated_at', 'slider', 'exception', 'views', 'comment', 'detail'
        ]

class StatusSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()
    def get_posts(self, obj):
        posts = Post.objects.filter(status=obj)
        serialized_posts = PostSerializer(posts, many=True).data
        return serialized_posts
    class Meta:
        model = Status
        fields = ['blog', 'posts']

class SubCatHeader(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = [
            'title',
            'slug',
        ]

class CatHeaderSerializer(serializers.ModelSerializer):
    subcategory = SubCatHeader(many=True, read_only=True)
    status = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            'id',
            'status',
            'title',
            'slug',
            'is_active',
            'subcategory',

        ]
