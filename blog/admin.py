from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'created_at')
    list_filter = ('published', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_at',)

    # 👇 allow created_at to show in the form
    fields = (
        'title',
        'slug',
        'author',
        'content',
        'published',
        'created_at',
    )

    def save_model(self, request, obj, form, change):
        # 👇 allow admin to override auto_now_add field
        if 'created_at' in form.cleaned_data:
            obj.created_at = form.cleaned_data['created_at']
        super().save_model(request, obj, form, change)
