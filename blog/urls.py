from . import views
from django.urls import path, re_path



app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('author/', views.author, name='author'),
    path('create_post/', views.createPost, name='create_post'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('post_list/', views.postList, name='post_list'),
]
