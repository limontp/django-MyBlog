from django import forms
from pagedown.widgets import AdminPagedownWidget
from .models import Post,Series

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = []


class AdminPostForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget)
    class Meta:
        model = Post
        fields = "__all__"