from django import forms
from .models import Category, Post

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'is_active']
#
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['cat', 'sub_cat', 'title', 'img', 'is_active', 'tags']  # Убираем 'slug'
