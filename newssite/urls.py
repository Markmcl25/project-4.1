from django.contrib import admin
from django.urls import path, include
from reddit.views import (
    PostList,
    PostDetail,
    custom_signup,
    signup_confirmation,
    LoggedOutView,
    category_view,
    edit_post,
    CreatePostView,
    UserPostListView,  # Include this view for user-specific posts
)
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Admin page for managing the app
    path('admin/', admin.site.urls),

    path('summernote/', include('django_summernote.urls')),

    # Home page showing all posts
    path('', PostList.as_view(template_name='home.html'), name='home'),

    # View for all posts by a user
    path('user/posts/', UserPostListView.as_view(), name='user_posts'),

    # Post list view (all public posts)
    path('posts/', PostList.as_view(template_name='post_list.html'), name='posts'),

    # Create post view
    path('create/', CreatePostView.as_view(), name='create_post'),

    # Category view
    path('category/<slug:category_slug>/', category_view, name='category'),

    # Post detail view
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),

    # Edit post page
    path('post/edit/<int:pk>/', edit_post, name='edit_post'),

    # Custom signup page
    path('accounts/signup/', custom_signup, name='signup'),

    # Signup confirmation page
    path('signup/confirmation/', signup_confirmation, name='signup_confirmation'),

    # Allauth URLs for authentication
    path('accounts/', include('allauth.urls')),

    # Logout view
    path('logout/', LogoutView.as_view(), name='logout'),

    # Login page
    path('accounts/login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),

    # Logged out page
    path('logged_out/', LoggedOutView.as_view(), name='logged_out'),

    # Password reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
