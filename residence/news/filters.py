from cProfile import label

import django_filters
from .models import *


class ArticleFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label='Название')
    cat = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE, verbose_name="Категория")
    sub_cat = models.ForeignKey(SubCategory, related_name="posts", on_delete=models.CASCADE,verbose_name="Подкатегория", null=True, blank=True)
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='Заголовок')
    steal = django_filters.BooleanFilter(field_name='steal', label='Заимствована')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", editable=False)
    tags = models.CharField("Теги", max_length=255, null=True, blank=True)
    slug = models.SlugField("Слаг", max_length=1000, unique=True, null=True, blank=True, editable=False)

    class Meta:
        model = Post
        fields = ['name', 'cat', 'title', 'steal', 'sub_cat','user', 'tags','slug']
