from locale import str
# from .forms import CommentUpdateForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from dash.models import APost
from . forms import PostUpdateForm

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    # paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        dpost = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = dpost.total_likes()

        liked = False
        if dpost.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context['liked'] = liked
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('news-feed3')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/about.html', context)

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
       post.likes.add(request.user)
       liked = True
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

# comment need to import Comment model
# class CommentView(LoginRequiredMixin, CreateView):
#     model = Comment
#     form_class = CommentUpdateForm
#     template_name = 'blog/add_comment.html'
#     # fields = '__all__'
#
#     def form_valid(self, form):
#         form.instance.post_id = self.kwargs['pk']
#         return super().form_valid(form)
#     success_url = reverse_lazy('blog-home')

def news_feed2(request):
    announcements = APost.objects.all().order_by('-date_posted')
    resident_post = Post.objects.all().order_by('-date_posted')
    return render(request, 'accounts/login_resident.html', {'announcements': announcements, 'resident_post': resident_post})

def news_feed3(request):
    announcement = APost.objects.all().order_by('-date_posted')
    resident_posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'blog/home.html', {'announcement': announcement, 'resident_posts': resident_posts})

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'blog/post_update_form.html'