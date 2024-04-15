from django.shortcuts import render, get_object_or_404, redirect

from .models import Article, Comment, Group_up
from article.forms import ArticleForm

# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article/article_list.html', {'articles': articles})


def article_detail(request, pk):
    article = get_object_or_404(Article.objects.all(), pk=pk)
    return render(request, 'articles/article_detail.html', {'article':article})


def article_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            article = form.instance
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'article/article_new.html',{'form':form})


def article_edit(request, pk):
    artcile = get_object_or_404(Article.objects.all(),pk=pk)

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            article = form.instance
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'article/article_edit.html',{'form':form, 'article':article})


def tag_list(request):
    tags = Article.objects.all()
    return render(request, 'tag/tag_list.html', {'tag': tags})

def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'comment/comments_list.html', {'Comments': comments})

def Groupup_list(request):
    group = Group_up.objects.all()
    return render(request, 'group/group_up.html', {'Group': group})
