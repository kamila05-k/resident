from django.db import models
from django.db.models import TextField
from django.utils.text import slugify
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
import threading
from .choices import STATUS_CHOICES
from django.contrib.auth import get_user_model
from smart_selects.db_fields import ChainedForeignKey

User = get_user_model()
current_user = threading.local()

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(unique=True, editable=False, verbose_name="Слаг")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    def save(self, *args, **kwargs):
        if not self.slug:  # Генерация slug только при первом сохранении
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    def __str__(self):
        return self.title

class SubCategory(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", related_name="subcategories")
    title = models.CharField("Название", max_length=255, null=True, blank=True)
    slug = models.SlugField("Слаг", blank=True, null=True, editable=False)
    def save(self, *args, **kwargs):
        if self.title and not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

class Status(models.Model):
    blog = models.CharField('Показать в блоке', max_length=255, null=True, blank=True, choices=STATUS_CHOICES)
    def __str__(self):
        return f'{self.blog}'
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Блог'

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", editable=False, null=True, blank=True)
    cat = ChainedForeignKey('Category', related_name="posts", on_delete=models.CASCADE, verbose_name="Категория")
    sub_cat = ChainedForeignKey('SubCategory',related_name="posts",on_delete=models.CASCADE,verbose_name="Подкатегория",null=True,blank=True,)
    status = ChainedForeignKey('Status',show_all=False,auto_choose=True,sort=True,related_name='posts',on_delete=models.CASCADE,null=True,blank=True,verbose_name='Показывать в блоге')
    title = models.CharField("Название", max_length=255)
    img = models.ImageField("Изображение", upload_to="images", blank=True, null=True)
    is_active = models.BooleanField("Опубликовать", default=False)
    tags = models.CharField("Теги", max_length=255, null=True, blank=True)
    slug = models.SlugField("Слаг", blank=True, null=True)
    created_at = models.DateTimeField("Дата добавления", auto_now_add=True, editable=False)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)
    views = models.PositiveIntegerField("Просмотры", default=0, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        else:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title


class PostDetail(models.Model):
    main = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="detail")
    description = RichTextUploadingField("Подробнее", config_name="default", null=True, blank=True)
    class Meta:
        verbose_name = "Контент"
        verbose_name_plural = "Контент"

class PostSlider(models.Model):
    slider = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="slider")
    image = models.ImageField("Изображение", null=True, blank=True)
    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдеры"

class PostFile(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, related_name="files")
    title = models.CharField("Заголовок", max_length=255, null=True, blank=True)
    file = models.FileField("Файл", upload_to="uploads/file", null=True, blank=True)
    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", verbose_name="Статья")
    user = models.CharField("Имя", max_length=30)
    comment = TextField("Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="Создано")
    is_active = models.BooleanField("Опубликовать", default=False)
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
    def __str__(self):
        return self.comment
