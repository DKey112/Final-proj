from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse,reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


from .models import Profile
from .forms import CustomPasswordChangeForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.
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

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user,  backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Your registration is successful")
            return redirect(reverse("gamenews:home"))
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, ('See you later. Bye!!'))
    return redirect('gamenews:home')

@login_required
def user_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been changed')
            return redirect('users:user_profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'u_form': u_form,'p_form': p_form}
    return render(request, 'users/profile.html', context)


class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name='users/change_password.html'
    success_url = reverse_lazy('users:success_password')
    
    