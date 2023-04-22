from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse,reverse_lazy
from django.views.decorators.csrf import csrf_exempt

from users.forms import CustomPasswordChangeForm

# Create your views here.
def user_login(request: HttpRequest) -> HttpResponse:
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Welcome to Games Shop')
            return redirect('gamenews:home')
        else:
            messages.success(request,'Oppps, An error has occurred ')
            return redirect('users:login')
    else:
        return render(request,'users/login.html')


# @csrf_exempt
def user_register(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"{user} registration is successful")
            return redirect("gamenews:home")
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def user_logout(request: HttpRequest) -> HttpResponse:
    logout(request)
    messages.success(request, ('See you later. Bye!!'))
    return redirect('gamenews:home')


class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name='users/change_password.html'
    success_url = reverse_lazy('user:success_password')

    def form_valid(self, form):
        form.save()
        self.request.session.flush()
        logout(self.request)
        messages.success(self.request, "Ваш пароль успешно изменен!!!")
        return super().form_valid(form)