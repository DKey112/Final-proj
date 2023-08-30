# Default lib 
from django.http import HttpRequest, HttpResponse,request
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.files.base import ContentFile
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Forms
from .forms import PostForm, CreateCommentForm

# Project models
from .models import Post, Game, Comment, Player, Team


#User models
from users.models import Profile



def all_game(request: HttpRequest) -> HttpResponse:
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "gamenews/home.html", context)
    

#Function for view game in dropdown menu "Cyber Spot Game"
def game_view(request,cats,*args, **kwargs):
    game_post = get_object_or_404(Game, slug=cats)
    posts_in_games = Post.objects.filter(game=game_post)
    game_inf = Game.objects.filter(slug=cats)
    game_menu = Game.objects.all()
    return render(request, "gamenews/game.html", 
    {'cats':cats, 'posts_in_games':posts_in_games,'game_inf':game_inf, 'game_menu':game_menu})
    

# Function to display all post
class PostListView(ListView):
    model = Post
    template_name = 'gamenews/home.html'
    context_object_name = 'posts'
    cats = Game.objects.all()
    ordering = ['-pub_date']

    def get_context_data(self,*args, **kwargs):
        game_menu = Game.objects.all()
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context['game_menu'] = game_menu
        return context

    def user_post(self,request, *args, **kwargs):
        u_post = Post.objects.filter(author=request.user)
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context['u_post'] = u_post
        return context


# Function to display a specific post 
class PostDetailView(DetailView):
    model = Post
    template_name = 'gamenews/post_detail.html'
    # context_object_name = 'posts'

    def get_context_data(self,*args, **kwargs):
        game_menu = Game.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context['game_menu'] = game_menu
        return context


# Function for create post
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

    def get_context_data(self,*args, **kwargs):
        game_menu = Game.objects.all()
        context = super(PostCreateView, self).get_context_data(*args, **kwargs)
        context['game_menu'] = game_menu
        return context


# Function for update post
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

    def get_context_data(self,*args, **kwargs):
        game_menu = Game.objects.all()
        context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
        context['game_menu'] = game_menu
        return context


# Function to remove post
class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'gamenews/post_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    def get_context_data(self,*args, **kwargs):
        game_menu = Game.objects.all()
        context = super(DeletePostView, self).get_context_data(*args, **kwargs)
        context['game_menu'] = game_menu
        return context

# Function for create comment in post
class CommentAddView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "gamenews/add_comment.html"
    form_class = CreateCommentForm
    # success_url = reverse_lazy('')

    # login_url = "profile:login"
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        form.save()
        return super().form_valid(form)

    def get_context_data(self,*args, **kwargs):
        game_menu = Game.objects.all()
        context = super(CommentAddView, self).get_context_data(*args, **kwargs)
        context['game_menu'] = game_menu
        return context

    
    

# Function for update comment in post
class UpdateCommentView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    context_object_name = "comment"
    template_name = "gamenews/update_comment.html"
    form_class = CreateCommentForm

    def get_context_data(self, **kwargs):
        game_menu = Game.objects.all()
        context = super(UpdateCommentView, self).get_context_data(**kwargs)
        context["game_menu"] =  game_menu
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.comment_id = self.kwargs['pk']
        form.save()
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False

# Function for remove comment in post
class DeleteCommentView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    context_object_name = "comment"
    template_name = "gamenews/delete_comment.html"
    success_url = reverse_lazy("gamenews:home")
    

    # def get_success_url(self):
    #         return request.META.get('HTTP_REFERER')

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text"] = "Delete comment"
        return context


# Function for searching data
def search_post(request):
    if request.method == 'POST':
        print(request.POST)
        searched = request.POST.get('searched', False)
        posts = Post.objects.filter(title__icontains=searched)
        games = Game.objects.filter(name__icontains= searched)
        players = Player.objects.filter(nickname__icontains=searched)
        teams = Team.objects.filter(team_name__icontains=searched)
        game_menu = Game.objects.all()
        return render(request, 'gamenews/search_post.html', {'searched':searched,'posts':posts, 'games':games,
                                                            'players':players,'teams':teams,'game_menu':game_menu})
        
    else:
        return render(request, 'gamenews/search_post.html') 
        
        

# Function for add like in the post 
@login_required
def post_likes(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=pk)
        if post.likes.filter(id=request.user.id):
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return redirect( request.META.get("HTTP_REFERER"))

@login_required
def favourite(request, pk):
    user = request.user.id
    post = get_object_or_404(Post, id=pk)
    profile = Profile.objects.get(user=user)
    if profile.favourite.filter(id=pk).exists():
        profile.favourite.remove(post)
    else:
        profile.favourite.add(post)
    return redirect( request.META.get("HTTP_REFERER"))



# Function to display all games 
class GameListView(ListView):
    model = Game
    template_name = 'gamenews/games_list.html'
    context_object_name = 'games'
    

    def get_context_data(self, **kwargs):
        game_menu = Game.objects.all()
        context = super(GameListView, self).get_context_data(**kwargs)
        context["game_menu"] =  game_menu
        return context
    

# Function to display all players
class PlayerListView(ListView):
    model = Player
    template_name = 'gamenews/players_list.html'
    context_object_name = 'players_list'
    cats = Game.objects.all()
    ordering = ['nickname']

    def get_context_data(self,*args, **kwargs):
        game_menu = Game.objects.all()
        context = super(PlayerListView, self).get_context_data(*args, **kwargs)
        context['game_menu'] = game_menu
        return context
    
# Function to display player profile
class PlayerDetailView(DetailView):
    model = Player
    template_name = 'gamenews/player_detail.html'
    

    def get_context_data(self,*args, **kwargs):
        game_menu = Game.objects.all()
        context = super(PlayerDetailView, self).get_context_data(*args, **kwargs)
        context['game_menu'] = game_menu
        return context
    

#Function to display all teams 
class TeamListView(ListView):
    model = Team
    template_name = 'gamenews/teams_list.html'
    context_object_name = 'teams_list'
    cats = Game.objects.all()
    ordering = ['team_name']

    def get_context_data(self,*args, **kwargs):
        game_menu = Game.objects.all()
        context = super(TeamListView, self).get_context_data(*args, **kwargs)
        context['game_menu'] = game_menu
        return context
    
    
# Function to display team profile
class TeamDetailView(DetailView):
    model = Team
    template_name = 'gamenews/team_detail.html'
    

    def get_context_data(self,*args, **kwargs):
        game_menu = Game.objects.all()
        context = super(TeamDetailView, self).get_context_data(*args, **kwargs)
        context['game_menu'] = game_menu
        return context