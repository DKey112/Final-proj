from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post


def index(request: HttpRequest) -> HttpResponse:
    context = {
        'posts':Post.objects.all()
    }
    return render(request, "gamenews/home.html", context)

class PostListView(ListView):
    model = Post
    template_name = 'gamenews/home.html'  
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template_name = 'gamenews/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # template_name = ''
    fields = ['title', 'content']
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)