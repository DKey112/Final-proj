from django.urls import path
from . import views
from .views import (PostListView, PostDetailView, PostCreateView, 
                    UpdatePostView, DeletePostView, GameView, 
                    CommentAddView, UpdateCommentView, DeleteCommentView)



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
    path('game/<str:cats>/', GameView, name='game'),
    path('search_post/', views.search_post, name='search_post'),
]