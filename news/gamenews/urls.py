from django.urls import path
from . import views
from .views import (PostListView, PostDetailView, PostCreateView, 
                    UpdatePostView, DeletePostView, GameView, 
                    CommentAddView, UpdateCommentView, DeleteCommentView,
                    GameListView)



app_name = "gamenews"

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('add_post/', PostCreateView.as_view(), name='add_post'),
    path('post/update/<int:pk>',UpdatePostView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete',DeletePostView.as_view(), name='post_delete'),
    path('post/<int:pk>/comment/', CommentAddView.as_view(), name='add_comment'),
    path('comment/<int:pk>/update/', UpdateCommentView.as_view(), name='update_comment'),
    path('comment/<int:pk>/delete/', DeleteCommentView.as_view(), name='delete_comment'),
    path('games/', GameListView.as_view(), name='games_list'),
    path('game/<str:cats>/', GameView, name='game'),
    path('search_post/', views.search_post, name='search_post'),
    path('player/', GameListView.as_view(), name='player_list'),
    path('player/<int:pk>', GameListView.as_view(), name='player_detail'),
    path('team/', GameListView.as_view(), name='team_list'),
    path('team/<int:pk>', GameListView.as_view(), name='team'),
    path('post_likes/<int:pk>', views.post_likes, name='likes'),
    
]