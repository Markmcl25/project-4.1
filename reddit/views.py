from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login
from django.urls import reverse_lazy
from .models import Post, Category, Comment
from .forms import PostForm, CommentForm, SignupForm  # Import CommentForm

# Class-based view for listing all posts (public view)
class PostList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-created_on')

def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # Pass categories to the template
        return context        

# Class-based view for listing posts by the logged-in user
class UserPostListView(ListView):
    model = Post
    template_name = 'post_list.html'  # Template to render posts
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.filter(author=self.request.user).order_by('-created_on')
        return Post.objects.none()

# Class-based view for creating a new post
class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the logged-in user as the author
        form.instance.status = 1  # Mark the post as published
        form.save()
        messages.success(self.request, 'Post created successfully!')
        return redirect(self.success_url)

# Class-based view for viewing a single post with comments
class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(approved=True)  # Approved comments only
        context['form'] = CommentForm()  # Provide the comment form
        return context

class CategoriesListView(ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'categories'

# Handle comment submission for a post
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Your comment has been added and is awaiting approval.')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    return redirect('post_detail', pk=post.pk)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', f'/post/{pk}/'))

# Class-based view for logged-out users
class LoggedOutView(TemplateView):
    template_name = 'logged_out.html'

# Function-based view for the custom signup page
def custom_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(request)
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
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('home')  # Replace 'home' with your desired redirect URL
        else:
            messages.error(request, 'Invalid username or password.')
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
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form, 'post': post})

# Category view
def category_list(request, category_slug=None):
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = Post.objects.filter(category=category, status=1)
        return render(request, 'category.html', {'category': category, 'posts': posts, 'categories': categories})
    else:
        return render(request, 'categories.html', {'categories': categories})

# Signup confirmation page
def signup_confirmation(request):
    return render(request, 'signup_confirmation.html')

@login_required
def upvote_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.upvotes.all():
        post.upvotes.remove(request.user)  # Remove upvote if it already exists
    else:
        post.upvotes.add(request.user)  # Add upvote
        post.downvotes.remove(request.user)  # Ensure user can't upvote and downvote simultaneously
    return JsonResponse({'upvotes': post.upvotes.count(), 'downvotes': post.downvotes.count(), 'total': post.total_votes()})

@login_required
def downvote_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.downvotes.all():
        post.downvotes.remove(request.user)  # Remove downvote if it already exists
    else:
        post.downvotes.add(request.user)  # Add downvote
        post.upvotes.remove(request.user)  # Ensure user can't upvote and downvote simultaneously
    return JsonResponse({'upvotes': post.upvotes.count(), 'downvotes': post.downvotes.count(), 'total': post.total_votes()})    

# Signup confirmation page
def signup_confirmation(request):
    return render(request, 'signup_confirmation.html')

@login_required
def upvote_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.upvotes.all():
        post.upvotes.remove(request.user)  # Remove upvote if it already exists
    else:
        post.upvotes.add(request.user)  # Add upvote
        post.downvotes.remove(request.user)  # Ensure user can't upvote and downvote simultaneously
    return JsonResponse({'upvotes': post.upvotes.count(), 'downvotes': post.downvotes.count(), 'total': post.total_votes()})

@login_required
def downvote_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.downvotes.all():
        post.downvotes.remove(request.user)  # Remove downvote if it already exists
    else:
        post.downvotes.add(request.user)  # Add downvote
        post.upvotes.remove(request.user)  # Ensure user can't upvote and downvote simultaneously
    return JsonResponse({'upvotes': post.upvotes.count(), 'downvotes': post.downvotes.count(), 'total': post.total_votes()})    