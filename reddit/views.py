from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login
from django.urls import reverse_lazy
from .models import Post, Category
from .forms import PostForm

# Class-based view for listing all posts (public view)
class PostList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-created_on')

# Class-based view for listing posts by the logged-in user
class UserPostListView(ListView):
    model = Post
    template_name = 'post_list.html'  # Template to render posts
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        # Ensure the user is authenticated
        if self.request.user.is_authenticated:
            # Filter posts created by the logged-in user
            return Post.objects.filter(author=self.request.user).order_by('-created_on')
        else:
            return Post.objects.none()  # Return empty queryset if user is not logged in

# Class-based view for creating a new post
class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('posts')  # Redirect to post list after a successful post creation

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the logged-in user as the author
        post = form.save()  # Save the post
        messages.success(self.request, 'Post created successfully!')  # Show success message
        return redirect(self.success_url)  # Redirect to the post list or home page

    def form_invalid(self, form):
        # In case of form errors, re-render the form with errors
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

# Class-based view for viewing a single post
class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

# Class-based view for logged-out users
class LoggedOutView(TemplateView):
    template_name = 'logged_out.html'

# Function-based view for the custom signup page
def custom_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(request)  # Pass the request to save
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "You have successfully signed up!")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})

# Custom login view
def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "You have successfully logged in!")
            return redirect('home')  # Redirect to homepage or other location
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

# Edit post view
@login_required
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

# Category view
def category_view(request, category_slug):
    # Get the category based on the slug
    category = get_object_or_404(Category, slug=category_slug)

    # Get all posts associated with the category
    posts = Post.objects.filter(category=category, status=1)  # Only show published posts

    # Render the category page with posts belonging to the selected category
    return render(request, 'category.html', {'category': category, 'posts': posts})

# Signup confirmation page
def signup_confirmation(request):
    return render(request, 'signup_confirmation.html')
