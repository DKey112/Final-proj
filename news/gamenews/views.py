from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.files.base import ContentFile
from django.urls import reverse, reverse_lazy

# Forms
from .forms import PostForm

# Project models
from .models import Post, Game


def index(request: HttpRequest) -> HttpResponse:
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "gamenews/home.html", context)
    


def GameView(request,cats,*args, **kwargs):
    game_post = get_object_or_404(Game, slug=cats)
    posts_in_games = Post.objects.filter(game=game_post)
    return render(request, "gamenews/game.html", {'cats':cats, 'posts_in_games':posts_in_games})



class PostListView(ListView):
    model = Post
    template_name = 'gamenews/home.html'
    context_object_name = 'posts'
    cats = Game.objects.all()
    ordering = ['-pub_date']

    def get_context_data(self,*args, **kwargs):
        game_menu = Game.objects.order_by('name')
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context['game_menu'] = game_menu
        return context

    def user_post(self,request, *args, **kwargs):
        u_post = Post.objects.filter(author=request.user)
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context['u_post'] = u_post
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'gamenews/post_detail.html'
    # context_object_name = 'posts'



class PostCreateView(LoginRequiredMixin, FormView):
    model = Post
    form_class = PostForm
    template_name = 'gamenews/post_form.html'
    success_url = reverse_lazy('gamenews:home')
    # fields = ['title', 'content','post_pic']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'gamenews/post_update.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'gamenews/post_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
