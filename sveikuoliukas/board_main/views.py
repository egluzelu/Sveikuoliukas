from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from forum import models
from django.contrib.auth import get_user_model


def index(request: HttpRequest) -> HttpResponse:
    context = {
        'users_count': get_user_model().objects.count(),
        'posts_count': models.Post.objects.count(),
        'comments_count': models.Comment.objects.count(),
    }
    return render(request, 'board_main/index.html', context)
