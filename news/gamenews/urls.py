from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, UpdatePostView, DeletePostView, GameView


app_name = "gamenews"

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('add_post/', PostCreateView.as_view(), name='add_post'),
    path('post/update/<int:pk>',UpdatePostView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete',DeletePostView.as_view(), name='post_delete'),
    path('game/<str:cats>/', GameView, name='game'),
]