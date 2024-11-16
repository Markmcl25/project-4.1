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
    CreatePostView,  # Import the correct class-based view
)
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Admin page for managing the app
    path('admin/', admin.site.urls),

    # Home page showing the post list (uses PostList view and home.html template)
    path('', PostList.as_view(template_name='home.html'), name='home'),

    # Create post view (form for creating posts)
    path('create/', CreatePostView.as_view(), name='create_post'),  # Updated to use CreatePostView

    # Category view (displays posts under a specific category)
    path('category/<slug:category_slug>/', category_view, name='category'),

    # Post detail view (individual post details page)
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),

    # Posts list view (for listing all posts using the posts.html template)
    path('posts/', PostList.as_view(template_name='posts.html'), name='posts'),

    # Edit post page
    path('post/edit/<int:pk>/', edit_post, name='edit_post'),

    # Custom signup page
    path('accounts/signup/', custom_signup, name='signup'),

    # Signup confirmation page (after a successful signup)
    path('signup/confirmation/', signup_confirmation, name='signup_confirmation'),

    # Allauth URLs for authentication
    path('accounts/', include('allauth.urls')),

    # Logout view (logs out the user)
    path('logout/', LogoutView.as_view(), name='logout'),

    # Login page (for signing in users)
    path('accounts/login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),

    # Logged out page (redirects after logging out)
    path('logged_out/', LoggedOutView.as_view(), name='logged_out'),

    # Password reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
