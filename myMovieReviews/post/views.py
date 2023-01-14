from django.shortcuts import render, redirect
from .models import Post

# Create your views here.

def post_list(request): #처음 페이지 리뷰 간략
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts})

def post_create(request, *args, **kwargs):
  if request.method == "POST":
    Post.objects.create(
      title=request.POST["title"],
      year=request.POST["year"],
      genre=request.POST["genre"],
      star=request.POST["star"],
      time=request.POST["time"],
      review=request.POST["review"],
      director=request.POST["director"],
      actor=request.POST["actor"],
    )
    return redirect("/")
  return render(request, "post/post_create.html")

def post_detail(request,pk): #게시글 상세정보 보기
    post = Post.objects.get(pk=pk)
    return render(request, 'post/post_detail.html', {'post': post})

def post_update(request, pk): #게시글 수정하기 
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.title=request.POST["title"]
        post.year=request.POST["year"]
        # post.pic=request.post["pic"],
        post.genre=request.POST["genre"]
        post.star=request.POST["star"]
        post.time=request.POST["time"]
        post.review=request.POST["review"]
        post.director=request.POST["director"]
        post.actor=request.POST["actor"]
        post.save()
        return redirect(f"/post/{post.pk}")
    return render(request, "post/post_update.html", {"post": post})

def post_delete(request, pk):  #게시글 삭제
    if request.method == "POST":
        post = Post.objects.get(id=pk)
        post.delete()
    return redirect("/")

