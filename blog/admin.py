from django.contrib import admin
from .models import Series, Post
from .forms import AdminPostForm

admin.site.register(Series)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = AdminPostForm

