from django.contrib import admin
from django.urls import path
from core.views import index, about


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('', index, name='index')
]
