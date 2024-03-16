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
from django.urls import reverse
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


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = models.Post
    template_name = 'forum/post_update.html'
    fields = ('name', 'description', 'image')

    def get_success_url(self) -> str:
        messages.success(self.request, 
            _('post updated succesfully').capitalize())
        return reverse('post_detail', args=[self.object.pk])

    def test_func(self) -> bool | None:
        return self.get_object().owner == self.request.user or self.request.user.is_superuser


def post_list(request: HttpRequest) -> HttpResponse:
    queryset = models.Post.objects
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
        post = self.get_object()
        comments_queryset = models.Comment.objects.filter(post=post)
        paginator = Paginator(comments_queryset, 5)
        page = self.request.GET.get('page', 1)

        try:
            comments = paginator.page(page)
        except PageNotAnInteger:
            comments = paginator.page(1)
        except EmptyPage:
            comments = paginator.page(paginator.num_pages)

        context['post_comments'] = comments
        context['comment_form'] = CommentForm()

        return context
            

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
    

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = models.Comment
    template_name = 'forum/comment_update.html'
    fields = ('body', 'image')

    def get_success_url(self) -> str:
        messages.success(self.request, 
            _('comment updated succesfully').capitalize())
        return reverse('post_detail', args=[self.get_object().post.pk])

    def test_func(self) -> bool | None:
        return self.get_object().owner == self.request.user or self.request.user.is_superuser
