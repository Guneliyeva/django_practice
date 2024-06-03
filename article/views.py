from django.shortcuts import render
from .models import Article

# Create your views here.
# def article(request):
#     return render(request, 'article.html')

def article_page(request):
    articles=Article.objects.all()
    return render(request, 'article.html', {'articles':articles}) #articles adinda artikillari article.html gonder