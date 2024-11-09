from django.shortcuts import render, redirect
from .forms import PostForm
from django.views import generic
from django.views.generic import DetailView
from .models import Post
from django.views.generic import TemplateView
from allauth.account.forms import SignupForm


# Class-based view for listing posts
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = 'index.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'  
    context_object_name = 'post'


class LoggedOutView(TemplateView):
    template_name = 'logged_out.html'    


# Function-based view for the custom signup page
def custom_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user data
            # Redirect to confirmation page after signup
            return redirect('signup_confirmation')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

# Sign up confirmation view
def signup_confirmation(request):
    return render(request, 'signup_confirmation.html')

# View for creating a new post
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to homepage after posting
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})
