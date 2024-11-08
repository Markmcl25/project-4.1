"""newssite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from reddit.views import PostList, custom_signup
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', PostList.as_view(), name='home'),  # This is the homepage displaying posts
    path('accounts/signup/', custom_signup, name='account_signup'),  # Custom signup page
    path('accounts/', include('allauth.urls')),  # Allauth URLs for authentication
    path('logout/', LogoutView.as_view(), name='logout'),  # Logout view
     path('signup_confirmation/', views.signup_confirmation, name='signup_confirmation'),
]

