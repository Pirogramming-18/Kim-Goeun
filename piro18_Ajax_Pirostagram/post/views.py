from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.http.response import JsonResponse
import json
# Create your views here.

def post_main (request):  #메인페이지
    post = Post.objects.all()
    form = CommentForm()
    ctx={
        'post': post,
        'form': form
    }
    return render (request, 'post/post_main.html', ctx)

def post_new(request, post=None):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect( 'post:post_main')
    else:
        form = PostForm(instance=post)
        ctx = {'form': form}
    return render(request, 'post/post_new.html', ctx)


#좋아요 버튼

@ csrf_exempt
def like_ajax (request):
    req = json.loads(request.body) # json.loads를 통해 json을 파이썬 형식으로 바꿔줌 {id:1, type:'like'} 을 아래처럼 바꿔줌
    post_id = req['id']  # id: 1 
    post = Post.objects.get(id=post_id)
    post.like = not(post.like)

    post.save()
    return JsonResponse({'id':post_id})  # #JsonResponse를 통해 형식을 바꿔서 보내줌 {id:1, type:'like'}  """

#댓글 버튼
@csrf_exempt
def comment_ajax(request):
    req = json.loads(request.body)
    post_id = req['id']
    comment_content = req['ct']
    comment = Comment()
    comment.post = get_object_or_404(Post, pk=post_id)
    comment.comment = comment_content
    comment.save()
    return JsonResponse({'id': post_id, 'ct': comment_content, 'comment_id': comment.id})


#삭제 ajax
@csrf_exempt
def delete_ajax(request):
    req = json.loads(request.body)
    comment_id = req['id']
    post_id = req['post_id']
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return JsonResponse({'id': comment_id, 'post_id': post_id})
