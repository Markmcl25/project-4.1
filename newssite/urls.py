from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from reddit.views import (
    PostList, PostDetail, custom_signup, signup_confirmation, create_post, LoggedOutView, category_view, edit_post
)
from django.contrib.auth.views import LogoutView, LoginView  


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),

    # Home page showing posts
    path('', PostList.as_view(), name='home'),
    path('home/', lambda request: redirect('home')),  # Redirect /home to the homepage

    # Create post view
    path('create_post/', create_post, name='create_post'),

    # Category view
    path('category/<slug:category_slug>/', category_view, name='category'),  # Directly using category_view

    # Post detail view
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),

    # Post Creation Page
    path('post/edit/<int:pk>/', edit_post, name='edit_post'),

    # Custom signup page
    path('accounts/signup/', custom_signup, name='account_signup'),

    # Allauth URLs for authentication
    path('accounts/', include('allauth.urls')),

    # Logout view (using Django's built-in logout)
    path('logout/', LogoutView.as_view(), name='logout'),  

    # Signup confirmation page
    path('signup_confirmation/', signup_confirmation, name='signup_confirmation'),

    # Login page
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),

    # Logged out page
    path('logged-out/', LoggedOutView.as_view(), name='logged_out'),
]
