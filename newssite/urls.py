from django.contrib import admin
from django.urls import path, include
from reddit.views import (
    PostList, PostDetail, custom_signup, signup_confirmation, create_post, LoggedOutView, category_view, edit_post
)
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    # Admin page for managing the app
    path('admin/', admin.site.urls),

    # Home page showing the post list (uses PostList view and home.html template)
    path('', PostList.as_view(template_name='home.html'), name='home'),

    # Create post view (form for creating posts)
    path('create/', create_post, name='create_post'),

    # Category view (displays posts under a specific category)
    path('category/<slug:category_slug>/', category_view, name='category'),

    # Post detail view (individual post details page)
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),

    # Posts list view (for listing all posts using the posts.html template)
    path('posts/', PostList.as_view(template_name='posts.html'), name='posts'),

    # Custom signup page
    path('accounts/signup/', custom_signup, name='signup'),

    # Signup confirmation page (after a successful signup)
    path('signup/confirmation/', signup_confirmation, name='signup_confirmation'),

    # Allauth URLs for authentication
    path('accounts/', include('allauth.urls')),

    # Logout view (logs out the user)
    path('logout/', LogoutView.as_view(), name='logout'),  

    # Login page (for signing in users)
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),

    # Logged out page (redirects after logging out)
    path('logged-out/', LoggedOutView.as_view(), name='logged_out'),
]
