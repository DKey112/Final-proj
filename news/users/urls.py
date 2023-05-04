from django.urls import path, include
from django.contrib.auth import views as auth_views

from users import views

app_name = "users"
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('user_profile/<int:pk>', views.ProfileView.as_view(), name='user_profile'),
    path('user_profile_edit/', views.user_profile, name='user_profile_edit'),
    path('login_user', views.user_login, name='login'),
    path('logout_user', views.user_logout, name='logout'),
    path('user_register', views.user_register, name='register'),
    path('change_password',views.CustomPasswordChangeView.as_view(), name='change_password'),
    path('success_password', auth_views.PasswordResetDoneView.as_view(template_name = 'users/success_password.html'), 
                                                                        name='success_password'),
]