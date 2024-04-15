from django.contrib import admin
from article.models import Article, Tag, Comment, Group_up
from django.contrib.auth.models import Group

# admin.site.register(Comment)
admin.site.register(Tag)
admin.site.unregister(Group)
admin.site.register(Comment)
admin.site.register(Group_up)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ['author']
    search_fields = ['title']

# admin.site.register(Article)


