from django.contrib import admin
from article.models import Article, Tag, Comment

# admin.site.register(Comment)
admin.site.register(Tag)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ['author']
    search_fields = ['title']

@admin.register(Comment)
class TagAdmin(admin.ModelAdmin):
    list_display = ['article', 'created_at']
    list_filter = ['created_at']
    search_fields = ('comment', 'artcile')

# admin.site.register(Article)


