from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import PostForm
from django.views import generic
from django.views.generic import DetailView, CreateView, TemplateView
from .models import Post, Category
from django.contrib.auth.decorators import login_required
from allauth.account.forms import SignupForm
from django.contrib import messages
from django.contrib.auth import login
from django.urls import reverse_lazy  # Needed for success URL in class-based views

# Class-based view for listing posts
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = 'posts.html'  # Use 'home.html' as the template
    context_object_name = 'posts'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add categories to the context
        context['categories'] = Category.objects.all()
        context['form'] = PostForm()  # Add the PostForm to the context to show the form on the same page
        return context

# Class-based view for creating a new post
class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('home')  # Redirect to home after successful post creation

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the logged-in user as the author
        return super().form_valid(form)

    def form_invalid(self, form):
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
