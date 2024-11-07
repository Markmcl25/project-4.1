from django.shortcuts import render
from django.views import generic
from .models import Post

# Class-based view for listing posts
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # You can add more context here if needed
        return context

# Function-based view for the home page
def home(request):
    return render(request, 'home.html')

# Function-based view for the custom signup page
def custom_signup(request):
    return render(request, 'registration/signup.html')  # Explicitly specify the template
