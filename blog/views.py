from django.shortcuts import render,get_object_or_404
from .models import BlogArticles

# Create your views here.

def index(request):
    return render(request,'blog/index.html')


def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, 'blog/titles.html', {'blogs':blogs})

def blog_article(request,id):
    # article = BlogArticles.objects.get(id=id)
    article = get_object_or_404(BlogArticles,id = id)
    return render(request,'blog/article.html',{'article':article})