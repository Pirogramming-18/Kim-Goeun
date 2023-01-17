from django.shortcuts import render, redirect
from posts.models import Post
from django.http.request import HttpRequest

def posts_list(request:HttpRequest, *args, **kwargs): #메인페이지 
    posts = Post.objects.all()
    # min_price = request.GET.get("min_price")
    # max_price = request.GET.get("max_price")
    # if min_price and max_price:
    #     posts = posts.filter(price__range=(min_price,max_price)) 
    return render(request, "posts/posts_list.html", {"posts":posts})

def posts_retrieve(request:HttpRequest, pk, *args, **kwargs):  #게시글 상세보기
    post = Post.objects.get(id=pk)
    return render(request, "posts/posts_retrieve.html", {'post':post})

def posts_create(request:HttpRequest, *args, **kwargs):
    if request.method == "POST":
        Post.objects.create(
            title=request.POST["title"],
            interest=request.POST["interest"],
            devtool=request.POST["devtool"],
            content=request.POST["content"],
            photo=request.FILES.get("photo",False)
        )
        return redirect("/")
    return render(request, "posts/posts_create.html")

def posts_delete(request:HttpRequest, pk, *args, **kwargs):
    if request.method == "POST":
        post = Post.objects.get(id=pk)
        post.delete()
    return redirect("/")

def posts_update(request:HttpRequest, pk, *args, **kwargs):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.title=request.POST["title"]
        post.interest=request.POST["interest"]
        post.devtool=request.POST["devtool"]
        post.content=request.POST["content"]
        post.photo=request.FILES.get("photo",False)
        post.save()
        return redirect(f"/posts/{post.id}")
    return render(request, "posts/posts_update.html", {"post":post})