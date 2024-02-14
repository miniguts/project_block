from django.shortcuts import render

from article.models import Article

# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article/article_list.html', {'articles': articles})