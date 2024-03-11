from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from . import models
from django.contrib.auth import get_user_model


def index(request: HttpRequest) -> HttpResponse:
    context = {
        'slide': models.Board.objects.all(),
        'users_count': get_user_model().objects.count(),
    }
    return render(request, 'board_main/index.html', context)
