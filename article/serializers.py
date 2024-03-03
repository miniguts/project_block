from article.models import Article, Tag

from rest_framework import serializers

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    tag = TagSerializer()

    class Meta:
        model = Article
        fields = '__all__'