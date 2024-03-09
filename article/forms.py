from django import forms

from article.models import Article, Tag

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'

class TagFrom(forms.ModelForm):

    class Meta:
        model = Tag
        fields = '__all__'