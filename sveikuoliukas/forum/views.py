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
from . import models
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm


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


class PostDetailView(generic.DetailView):
    model = models.Post
    template_name = 'forum/post_detail.html'
    fields = ('name', 'description', 'image')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context
    

class CommentListView(generic.ListView):
    model = models.Comment
    template_name = 'forum/comment_list.html'
    fields = ('name', 'description', 'image')

    def get_queryset(self):
        post = get_object_or_404(models.Post, pk=self.kwargs['pk'])
        return models.Comment.objects.filter(post=post)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(models.Post, pk=self.kwargs['pk'])
        return context
    

class CommentDetailView(generic.DetailView):
    model = models.Comment
    template_name = 'forum/comment_detail.html'
    fields = ('body', 'image')
    context_object_name = 'comment' 


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Comment
    template_name = 'forum/comment_create.html'
    form_class = CommentForm

    def form_valid(self, form):
        post = get_object_or_404(models.Post, pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        messages.success(self.request, 
            _('comment created succesfully').capitalize())
        return reverse('post_detail', kwargs={'pk': self.kwargs['pk']})

