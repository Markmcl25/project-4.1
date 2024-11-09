from django.contrib import admin
from django.urls import path, include
from reddit.views import PostList, PostDetail, custom_signup, signup_confirmation, create_post
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),

    # Home page showing posts
    path('', PostList.as_view(), name='home'),  # This serves the home page

    # Create post view
    path('create_post/', create_post, name='create_post'),

    # Post detail view
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),

    # Custom signup page
    path('accounts/signup/', custom_signup, name='account_signup'),

    # Allauth URLs for authentication
    path('accounts/', include('allauth.urls')),

    # Logout view
    path('logout/', LogoutView.as_view(next_page='logged_out'), name='logout'),

    # Signup confirmation page
    path('signup_confirmation/', signup_confirmation, name='signup_confirmation'),
]
