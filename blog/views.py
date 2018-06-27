from django.shortcuts import render
from .models import BlogArticles
# Create your views here.

def index(request):
    return render(request,'blog/index.html')


def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, 'blog/titles.html', {'blogs':blogs})