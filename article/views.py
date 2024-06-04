from django.shortcuts import render
from .models import Article

# Create your views here.
# def article(request):
#     return render(request, 'article.html')

def article_page(request):
    articles=Article.objects.all()
    return render(request, 'article.html', {'articles':articles}) #articles adinda artikillari article.html gonder

def our__blogs__view(request):
    articles = Article.objects.all()
    return render(request,'blogs.html', {'articles': articles})

def my__blogs__view(request):
    articles = Article.objects.all()
    return render(request,'my-blogs.html', {'articles': articles})