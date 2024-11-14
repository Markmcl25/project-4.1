from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import PostForm
from django.views import generic
from django.views.generic import DetailView
from .models import Post, Category
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from allauth.account.forms import SignupForm
from . import views
from django.contrib import messages
from django.contrib.auth import login

# Class-based view for listing posts
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = 'home.html'  # Use 'home.html' as the template
    context_object_name = 'posts'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add categories to the context
        context['categories'] = Category.objects.all()
        return context

def post_list_and_create(request):
    # Handle new post creation
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user  # You can set the author to the logged-in user
            new_post.save()  # Save the new post to the database
            return redirect('posts')  # Redirect back to the posts page to show the new post
    else:
        form = PostForm()  # Empty form for new post creation

    # Fetch all posts to display them on the page
    posts = Post.objects.all().order_by('-created_on')

    return render(request, 'posts.html', {'form': form, 'posts': posts})        


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class LoggedOutView(TemplateView):
    template_name = 'logged_out.html'

# Function-based view for the custom signup page
def custom_signup(request):
    if request.method == 'POST':
        form = SignupForm(data=request.POST)  # Pass data without the request parameter
        if form.is_valid():
            user = form.save()  # Don't pass the request here, Allauth handles it internally
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # Explicitly specify the backend
            messages.success(request, "You have successfully signed up!")
            return redirect('signup_confirmation')
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = SignupForm()  # Initialize the form without passing request

    return render(request, 'account/signup.html', {'form': form})
 
# View for creating a new post
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the logged-in user as the author
            post.save()
            return redirect('home')  # Redirect to the home page after saving the post
    else:
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})

# Edit post view
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)  # Redirect to the post detail page after saving
    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form, 'post': post})

def category_view(request, category_slug):
    # Get the category based on the slug
    category = get_object_or_404(Category, slug=category_slug)

    # Get all posts associated with the category
    posts = Post.objects.filter(category=category, status=1)  # Only show published posts

    # Render the category page with posts belonging to the selected category
    return render(request, 'category.html', {'category': category, 'posts': posts})

def signup_confirmation(request):
    return render(request, 'signup_confirmation.html')
