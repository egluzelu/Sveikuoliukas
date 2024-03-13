from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('detail/', views.user_detail, name='user_detail_current'),
    path('detail/<str:username>/', views.user_detail, name='user_detail'),
    path('update/', views.user_update, name='user_update'),
    path('received/', views.chat_list_received, name='chat_list_received'),  
    path('send/', views.chat_list_send, name='chat_list_send'),  
    path('create/', views.ChatCreateView.as_view(), name='chat_create'),
]
