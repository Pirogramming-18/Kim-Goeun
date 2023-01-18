from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post, Tool
from django.http.request import HttpRequest


# post view 설정

def posts_list(request:HttpRequest, *args, **kwargs): #메인페이지 
    posts = Post.objects.all()
    return render(request, "posts/posts_list.html", {"posts":posts})

def posts_retrieve(request:HttpRequest, pk, *args, **kwargs):  #게시글 상세보기
    post = Post.objects.get(id=pk)
    return render(request, "posts/posts_retrieve.html", {'post':post})

def posts_create(request:HttpRequest, *args, **kwargs):
    tools=Tool.objects.all()
    if request.method == "POST":
        tool_pk=request.POST.get('tool', False)
        try:
            toole = Tool.objects.get(pk=tool_pk)
        except Tool.DoesNotExist:
            toole = None
        Post.objects.create(
            title=request.POST["title"],
            interest=request.POST["interest"],
            devtool=toole,
            content=request.POST["content"],
            photo=request.FILES.get("photo",False),
        )
        latest= Post.objects.last()
        return redirect(f"/posts/{latest.pk}/")
    return render(request, "posts/posts_create.html", {'tools':tools})

def posts_delete(request:HttpRequest, pk, *args, **kwargs):
    if request.method == "POST":
        post = Post.objects.get(id=pk)
        post.delete()
    return redirect("/")

def posts_update(request:HttpRequest, pk, *args, **kwargs):
    post = Post.objects.get(id=pk)
    tools=Tool.objects.all()
    context={
        'post':post,
        'tools':tools,
         }
    if request.method == "POST":
        post.title=request.POST["title"]
        post.interest=request.POST["interest"]
        post.devtool=request.POST["devtool"]
        post.content=request.POST["content"]
        post.photo=request.FILES.get("photo",False)
        post.save()
        return redirect(f"/posts/{post.id}")
    return render(request, "posts/posts_update.html", {'context':context})

# devtool view 설정

def devtool_list(request:HttpRequest, *args, **kwargs): #메인페이지 
    tools = Tool.objects.all()
    return render(request, "posts/devtool_list.html", {"tools":tools})

def devtool_retrieve(request:HttpRequest, pk, *args, **kwargs):  #게시글 상세보기
    tool = Tool.objects.get(id=pk)
    return render(request, "posts/devtool_retrieve.html", {'tool':tool})

def devtool_create(request:HttpRequest, *args, **kwargs):
    if request.method == "POST":
        Tool.objects.create(
            name=request.POST["name"],
            type=request.POST["type"],
            tool_content=request.POST["tool_content"],
        )
        return redirect("/posts/devtool_list")
    return render(request, "posts/devtool_create.html")

def devtool_delete(request:HttpRequest, pk, *args, **kwargs):
    if request.method == "POST":
        tool = Tool.objects.get(id=pk)
        try:
            toold = Tool.objects.get(pk=tool)
        except Tool.DoesNotExist:
            toold = None
        tool.delete()
    return redirect("/posts/devtool_list")

def devtool_update(request:HttpRequest, pk, *args, **kwargs):
    tool = Tool.objects.get(id=pk)
    if request.method == "POST":
        tool.name=request.POST["name"]
        tool.type=request.POST["type"]
        tool.tool_content=request.POST["tool_content"]
        tool.save()
        return redirect(f"/posts/devtool_list/{tool.id}")
    return render(request, "posts/devtool_update.html", {"tool":tool})