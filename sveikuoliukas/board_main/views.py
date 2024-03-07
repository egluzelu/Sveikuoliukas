
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _
from . import models

def index(request: HttpRequest) -> HttpResponse:
    context = { 
        'board_description': models.Board.objects
    }
    return render(request, 'board_main/index.html', context)
  

