from django.conf import settings
from django.conf.urls.static import static
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
    add_comment,
    upvote_post,
    downvote_post,
    UserPostListView,
)
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Summernote rich text editor
    path('summernote/', include('django_summernote.urls')),

    # Home page (all posts)
    path('', PostList.as_view(template_name='home.html'), name='home'),

    # User-specific posts
    path('user/posts/', UserPostListView.as_view(), name='user_posts'),

    # Public post list
    path('posts/', PostList.as_view(template_name='post_list.html'), name='posts'),

    # Create post
    path('create/', CreatePostView.as_view(), name='create_post'),

    # Category view
    path('category/<slug:category_slug>/', category_view, name='category'),

    # Single post detail
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),

    # Edit post
    path('post/edit/<int:pk>/', edit_post, name='edit_post'),

    # Add comment to post
    path('post/<int:pk>/comment/', add_comment, name='add_comment'),

    # Voting system
    path('post/<int:pk>/upvote/', upvote_post, name='upvote_post'),
    path('post/<int:pk>/downvote/', downvote_post, name='downvote_post'),

    # Custom signup
    path('accounts/signup/', custom_signup, name='signup'),

    # Signup confirmation
    path('signup/confirmation/', signup_confirmation, name='signup_confirmation'),

    # Authentication (Allauth)
    path('accounts/', include('allauth.urls')),

    # Logout
    path('logout/', LogoutView.as_view(), name='logout'),

    # Login
    path('accounts/login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),

    # Logged out page
    path('logged_out/', LoggedOutView.as_view(), name='logged_out'),

    # Password reset
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
