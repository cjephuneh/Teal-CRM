from django.contrib import admin
from django.urls import path, include
from core.views import index, about
from userprofile.views import signup
from django.contrib.auth import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('sign-up/', signup, name='signup'),
    path('log-in/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('log-out/', views.LogoutView.as_view(), name='logout'),
    path('dashboard/', include('dashboard.urls')),
    path('', index, name='index')
]
      