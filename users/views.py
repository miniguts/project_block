from django.shortcuts import render

from users.models import User

# Create your views here.
def user_list(request):
    users = User.objects.all()
    return render(request, 'article/article_list.html', {'users': users})