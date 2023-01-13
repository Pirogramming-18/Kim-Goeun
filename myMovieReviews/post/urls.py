from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/',views.post_create, name='post_create'), #게시글 작성하기 
    path('post/<int:pk>',views.post_detail, name='post_detail'),  #게시글 상세보기 
    path('post/<int:pk>/update',views.post_update, name='post_update'), #게시글 수정
    path('post/<int:pk>/delete', views.post_delete, name='post_delete'), #게시글 삭제 
]