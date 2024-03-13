from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext_lazy as _
from . import forms
from . import models
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseForbidden
from django.db.models import Q



User = get_user_model()

def signup(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Thank you! You can now log in with your credentials."))
            return redirect('login')
    else:
        form = forms.CreateUserForm()
    return render(request, 'user_profile/signup.html', {
        'form': form,
    })


@login_required
def user_detail(request: HttpRequest, username: str | None = None) -> HttpResponse:
    if username:
        user = get_object_or_404(User, username=username)
    else:
        user = request.user
    return render(request, 'user_profile/user_detail.html', {
        'object': user,
    })


@login_required
def user_update(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form_user = forms.UserForm(request.POST, instance=request.user)
        form_profile = forms.ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form_user.is_valid() and form_profile.is_valid():
            form_user.save()
            form_profile.save()
            messages.success(request, _("profile edited successfully").capitalize())
            return redirect('user_detail_current')
    else:
        form_user = forms.UserForm(instance=request.user)
        form_profile = forms.ProfileForm(instance=request.user.profile)
    return render(request, 'user_profile/user_update.html', {
        'form_user': form_user,
        'form_profile': form_profile,
    })


class ChatCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Chat
    template_name = 'user_profile/chat_create.html'
    form_class = forms.ChatForm

    def get_success_url(self) -> str:
        messages.success(self.request, _('message created successfully').capitalize())
        return reverse('chat_list_send')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.save()
        form.instance.receiver.add(self.request.user)
        form.instance.save()
        form.instance.receiver_owner.add(self.request.user)
        form.instance.save()
        return super().form_valid(form)


@login_required
def chat_list_received(request: HttpRequest) -> HttpResponse:
    user_chats = models.Chat.objects.filter(receiver=request.user)
    owner_username = request.GET.get('owner')
    receiver_username = request.GET.get('receiver')

    if owner_username:
        owner = get_object_or_404(get_user_model(), username=owner_username)
        user_chats = user_chats.filter(owner=owner)

    if receiver_username:
        receiver = get_object_or_404(get_user_model(), username=receiver_username)
        user_chats = user_chats.filter(receiver=receiver)

    search_name = request.GET.get('search_name')
    if search_name:
        user_chats = user_chats.filter(title__icontains=search_name)

    context = {
        'chat_list_received': user_chats,
        'user_list': get_user_model().objects.all().order_by('username'),
        'next': reverse('chat_list_received') + '?' + \
            '&'.join([f"{key}={value}" for key, value in request.GET.items()]),
    }

    return render(request, 'user_profile/chat_list_received.html', context)


@login_required
def chat_list_send(request: HttpRequest) -> HttpResponse:
    owner_chats = models.Chat.objects.filter(owner=request.user)
    owner_username = request.GET.get('owner')
    receiver_username = request.GET.get('receiver')
  
    if owner_username:
        owner = get_object_or_404(get_user_model(), username=owner_username)
        owner_chats = owner_chats.filter(owner=owner)

    if receiver_username:
        receiver = get_object_or_404(get_user_model(), username=receiver_username)
        owner_chats = owner_chats.filter(receiver=receiver)

    search_name = request.GET.get('search_name')
    if search_name:
        owner_chats = owner_chats.filter(title__icontains=search_name)

    context = {
        'chat_list_send': owner_chats,
        'user_list': get_user_model().objects.all().order_by('username'),
        'next': reverse('chat_list_send') + '?' + \
            '&'.join([f"{key}={value}" for key, value in request.GET.items()]),
    }

    return render(request, 'user_profile/chat_list_send.html', context)
