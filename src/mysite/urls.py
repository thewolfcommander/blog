from django.urls import path, include
from django.contrib import admin

from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('login/', views.LoginView.as_view(), name='login', kwargs={'next_page': '/'}),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
