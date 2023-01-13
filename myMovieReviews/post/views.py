from django.shortcuts import render, redirect
from .models import Post

# Create your views here.

def post_list(request): #처음 페이지 리뷰 간략
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts})

def post_create(request):  #게시글 새로 작성 (add movie review)
    if request.method == "post":
       Post.objects.create(
            title=request.Post["title"],
            year=request.Post["year"],
            pic=request.Post["pic"],
            genre=request.Post["genre"],
            star=request.Post["star"],
            time=request.Post["time"],
            content=request.Post["content"],
            director=request.Post["director"],
            actor=request.Post["actor"],)
       return redirect("/")
    return render(request, "/post_create.html")

def post_detail(request,pk): #게시글 상세정보 보기
    post = Post.objects.get(pk=pk)
    return render(request, 'post/post_detail.html', {'post': post})

def post_update(request, pk): #게시글 수정하기 
    post = Post.objects.get(id=pk)
    if request.method == "post":
        post.title=request.post["title"],
        post.year=request.post["year"],
        post.pic=request.post["pic"],
        post.genre=request.post["genre"],
        post.star=request.post["star"],
        post.time=request.post["time"],
        post.content=request.post["content"],
        post.director=request.post["director"],
        post.actor=request.post["actor"],
        post.save()
        return redirect(f"/post/{post.id}")
    return render(request, "post/post_update.html", {"post": post})

def post_delete(request, pk):  #게시글 삭제
    if request.method == "post":
        post = Post.objects.get(id=pk)
        post.delete()
    return redirect("/")

