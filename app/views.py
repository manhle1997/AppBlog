from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from django.http import HttpResponseRedirect


class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'postlist'


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        comment_form = CommentForm()

    return render(request, 'post_detail.html', {'comment_form': comment_form})
# Create your views here.
