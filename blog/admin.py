from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'published_at')
    list_filter = ('published', 'published_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-published_at',)

    fields = (
        'title',
        'slug',
        'author',
        'content',
        'published',
        'published_at',
    )

