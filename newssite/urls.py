from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from reddit.views import PostList, PostDetail, custom_signup, signup_confirmation, create_post, LoggedOutView
from django.contrib.auth.views import LogoutView  # Make sure this is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),

    # Home page showing posts
    path('', PostList.as_view(), name='home'),
    path('home/', lambda request: redirect('home')),  # Redirect /home to the homepage

    # Create post view
    path('create_post/', create_post, name='create_post'),

    # Post detail view
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),

    # Custom signup page
    path('accounts/signup/', custom_signup, name='account_signup'),

    # Allauth URLs for authentication
    path('accounts/', include('allauth.urls')),

    # Logout view (using Django's built-in logout)
    path('logout/', LogoutView.as_view(), name='logout'),  # Make sure this is correctly defined

    # Signup confirmation page
    path('signup_confirmation/', signup_confirmation, name='signup_confirmation'),

    # Logged out page
    path('logged-out/', LoggedOutView.as_view(), name='logged_out'),
]
