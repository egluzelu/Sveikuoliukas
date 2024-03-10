from typing import Any
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views import generic
from . import models, forms
from django.urls import reverse
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Post
    template_name = 'forum/post_create.html'
    fields = ('name', 'description', 'image')

    
    def get_success_url(self) -> str:
        messages.success(self.request, 
            _('post created succesfully').capitalize())
        return reverse('post_list')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,
        UserPassesTestMixin,
        generic.UpdateView,
    ):
    model = models.Post
    template_name = 'forum/post_update.html'
    fields = ('name', 'description', 'image')

    def get_success_url(self) -> str:
        messages.success(self.request, 
            _('post updated succesfully').capitalize())
        return reverse('post_list')

    def test_func(self) -> bool | None:
        return self.get_object().owner == self.request.user or self.request.user.is_superuser


def post_list(request: HttpRequest) -> HttpResponse:
    queryset = models.Post.objects
    owner_username = request.GET.get('owner')
    if owner_username:
        owner = get_object_or_404(get_user_model(), username=owner_username)
        queryset = queryset.filter(owner=owner)
    search_name = request.GET.get('search_name')
    if search_name:
        queryset = queryset.filter(name__icontains=search_name)

    page = request.GET.get('page', 1)
    paginator = Paginator(queryset.all(), 5)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'post_list': posts,
        'user_list': get_user_model().objects.all().order_by('username'),
        'next': reverse('post_list') + '?' + \
            '&'.join([f"{key}={value}" for key, value in request.GET.items()]),
    }

    return render(request, 'forum/post_list.html', context)


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'forum/post_detail.html', {
        'post': get_object_or_404(models.Post, pk=pk),
    })
