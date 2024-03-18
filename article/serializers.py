from article.models import Article, Tag, Comment

from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    # tag = TagSerializer(source='tag_name', many=True)
    comment = CommentSerializer(source='comments', many=True)

    class Meta:
        model = Article
        fields = '__all__'



