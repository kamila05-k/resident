from django.contrib import admin
from .models import *
from .forms import *


class SubCategoryInline(admin.StackedInline):
    model = SubCategory
    extra = 1


class PostSliderInline(admin.StackedInline):
    model = PostSlider
    extra = 1


class PostDetailInline(admin.StackedInline):
    model = PostDetail
    extra = 1


class PostFileInline(admin.StackedInline):
    model = PostFile
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoryInline]
    list_display = ['formatted_title', 'is_active']
    list_display_links = ['formatted_title']
    list_per_page = 8

    def formatted_title(self, obj):
        return obj.title.upper()
    formatted_title.short_description = "Название"


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ["blog"]
    list_display_links = ["blog"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostDetailInline, PostSliderInline, PostFileInline]
    list_display = ("title", "cat", "is_active", "views", "created_at", "status")
    prepopulated_fields = {"slug": ("title",)}
    fields = ("user", "cat", "sub_cat", "title", "slug", "img", "tags", "is_active", "status", "views")
    readonly_fields = ("user", "views")
    list_filter = ("is_active", "status", "created_at")
    search_fields = ("title", "cat__title")
    list_per_page = 10


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("post__title", "user__username")
    readonly_fields = ("created_at",)
    list_per_page = 20
