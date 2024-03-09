from article.models import Article, Tag, Comment

from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    tag = TagSerializer(source='tags' ,many=True)
    coment = CommentSerializer(source='comments' ,many=True)

    class Meta:
        model = Article
        fields = '__all__'