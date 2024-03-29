from django.contrib import admin

from authorization.models import User

# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'date_joined')