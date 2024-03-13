from django.urls import path
from . import views

urlpatterns = [  
    path('', views.post_list, name='post_list'), 
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'), 
    path('<int:pk>/create/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
]

