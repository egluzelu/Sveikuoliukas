from django.urls import path
from . import views

urlpatterns = [  
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'), 
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
]