from django.urls import path
from . import views

app_name ="posts"

urlpatterns= [
    path("", views.posts_list, name="list"),
    path("posts/create/", views.posts_create, name="create"),
    path("posts/<int:pk>/",views. posts_retrieve,  name="retrieve"),
    path("posts/<int:pk>/update/", views.posts_update,  name="update"),
    path("posts/<int:pk>/delete/", views.posts_delete,  name="delete"),

    path("posts/devtool_list", views.devtool_list, name="devtool_list"),
    path("posts/devtool_create", views.devtool_create, name="devtool_create"),
    path("posts/devtool_list/<int:pk>",views. devtool_retrieve,  name="devtool_retrieve"),
    path("posts/devtool_list/<int:pk>/update", views.devtool_update,  name="devtool_update"),
    path("posts/devtool_list/<int:pk>/delete", views.devtool_delete,  name="devtool_delete"),
]