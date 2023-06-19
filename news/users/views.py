from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse,reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView


from .models import Profile
from gamenews.models import Post, Game
from .forms import CustomPasswordChangeForm, UserUpdateForm, ProfileUpdateForm

#Function for login user
def user_login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Welcome to GameNews')
            return redirect('gamenews:home')
        else:
            messages.success(request,'Oppps, An error has occurred ')
            return redirect('users:login')
    else:
        return render(request,'users/login.html')

# Function for registration new user
def user_register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user,  backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Your registration is successful")
            return redirect(reverse("gamenews:home"))
    return render(request, 'users/register.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, ('See you later. Bye!!'))
    return redirect('gamenews:home')

#Function for view user profile
class ProfileView(DetailView):
    model = Profile
    # context_object_name = "profile"
    template_name = "users/profile.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context["u_post"] = Post.objects.filter(author=self.object.user)
        context['game_menu'] = Game.objects.all()
        context['favourites'] =  self.object.favourite.all()
        return context
    

# Function for presentation and edit information in user profile
@login_required
def user_profile(request):
    current_user = request.user
    user_list = Post.objects.filter(author=current_user)
    game_menu = Game.objects.all()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been changed')
            return redirect('users:user_profile_edit')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {'u_form': u_form,'p_form': p_form,'u_post':user_list,'game_menu':game_menu}
    return render(request, 'users/profile_edit.html', context)


# Function for change password
class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name='users/change_password.html'
    success_url = reverse_lazy('users:success_password')
    

