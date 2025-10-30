from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_list(request):
    posts = BlogPost.objects.filter(published=True)
    hero_images = [
        "propertyA/Cambridge1.png",
            "propertyA/Cambridge2.png",
            "propertyA/Cambridge_Photos_5.png",
            "propertyA/Cambridge_Photos_8.png",
            "propertyA/Cambridge_Photos_7.png",
    ]
    return render(request, 'blog/list.html', {'posts': posts, 'hero_images': hero_images})


def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/detail.html', {'post': post})
