from .models import *
from django import forms
from django.forms import ModelForm
from django_ckeditor_5.widgets import CKEditor5Widget


#Post(blog) Form
class BlogForm(ModelForm):
    class Meta:
        model = Post
        fields = ("title", "image", "status", "content")
        widgets = {
            "content": CKEditor5Widget(config_name="default")
        }