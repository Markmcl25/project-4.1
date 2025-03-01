from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from reddit.views import (
    PostList,
    PostDetail,
    custom_signup,
    custom_login,
    signup_confirmation,
    LoggedOutView,
    category_list,
    edit_post,
    CreatePostView,
    add_comment,
    upvote_post,
    downvote_post,
    UserPostListView,
    category_page,
)
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # Summernote Rich Text Editor
    path('summernote/', include('django_summernote.urls')),

    # Home Page (All Posts)
    path('', PostList.as_view(template_name='home.html'), name='home'),  # Ensure template matches

    # User-Specific Posts
    path('user/posts/', UserPostListView.as_view(), name='user_posts'),

    # Public Post List
    path('posts/', PostList.as_view(template_name='post_list.html'), name='posts'),

    # Create Post
    path('create/', CreatePostView.as_view(), name='create_post'),

    # Categories
    path('categories/', category_list, name='categories'),
    path('category/<str:category_name>/', category_page, name='category_page'),  # Removed duplicate slug route

    # Post Details and Editing
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post/edit/<int:pk>/', edit_post, name='edit_post'),

    # Add Comment to Post
    path('post/<int:pk>/comment/', add_comment, name='add_comment'),

    # Voting System
    path('post/<int:pk>/upvote/', upvote_post, name='upvote_post'),
    path('post/<int:pk>/downvote/', downvote_post, name='downvote_post'),

    # Authentication
    path('accounts/signup/', custom_signup, name='signup'),
    path('signup/confirmation/', signup_confirmation, name='signup_confirmation'),
    path('accounts/login/', custom_login, name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),  # Changed for consistency

    # Password Reset (Django Built-in Views)
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Allauth URLs (for social authentication)
    path('accounts/', include('allauth.urls')),
]

# Serve Media Files During Development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
