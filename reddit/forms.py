from django import forms
from .models import Post, Category, Comment
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class PostForm(forms.ModelForm):
    # Define the category field with a custom widget
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select Category",  # Placeholder text for the dropdown
        required=True,
        widget=forms.Select(attrs={'class': 'form-select', 'aria-label': 'Category'})
    )

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter content'}))
    featured_image = forms.ImageField(
        required=False,  # Allow the field to be optional
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'featured_image']
    
    # Define the title field with a custom widget and placeholder
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter post title', 
            'aria-label': 'Post Title'
        })
    )

    # Define the subtitle field with a custom widget and placeholder
    subtitle = forms.CharField(
        max_length=300,
        required=False,  # Optional field
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter a subtitle (optional)', 
            'aria-label': 'Subtitle'
        })
    )
    
    # Define the content field with a custom widget and placeholder
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'rows': 4, 
            'placeholder': 'Enter post content...', 
            'aria-label': 'Post Content'
        })
    )
    
    # Define the URL field with a custom widget and placeholder
    url = forms.URLField(
        required=False,  # Optional field
        widget=forms.URLInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter external URL (optional)', 
            'aria-label': 'External URL'
        })
    )
    
    # Define the image field with a custom widget
    featured_image = forms.ImageField(
        required=False,  # Optional field
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'content', 'category', 'url', 'featured_image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Your email'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Your comment',
                'rows': 4,  # Adjust rows to reduce initial height
                'style': 'max-height: 150px; overflow-y: auto;',
            }),
        }
