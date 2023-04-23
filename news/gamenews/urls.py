from django.urls import path
from . import views
from .views import PostDetailView, PostCreateView


app_name = "gamenews"

urlpatterns = [
    path("", views.index, name="home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('add_post/', PostCreateView.as_view(), name='add_post'),
]