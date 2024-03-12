from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('detail/', views.user_detail, name='user_detail_current'),
    path('detail/<str:username>/', views.user_detail, name='user_detail'),
    path('update/', views.user_update, name='user_update'),
    path('chat/list/', views.chat_list, name='chat_list'),  
    path('chat/detail/', views.ChatDetailView.as_view(), name='chat_detail'), 
    path('chat/create/', views.ChatCreateView.as_view(), name='chat_create'),
]
