from django.urls import path, include
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    # UserPostListView
# like_post,
LikeView,
# CommentView,
)
from . import views

urlpatterns = [
    path('blog', PostListView.as_view(), name='blog-home'),
    # path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about', views.about, name='blog-about'),
    path('dash/', include('dash.urls')),

    # path('like/', like_post, name='like_post'),
    path('like/<int:pk>', views.LikeView, name="like_post"),
#     comment
# path('post/<int:pk>/comment/new/', CommentView.as_view(), name='add_comment'),
    path('residents/newsfeed/', views.news_feed2, name='news-feed2'),
path('new/residents/newsfeed/', views.news_feed3, name='news-feed3'),
]