from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Post, Category, Comment, UserProfile
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    avatar = forms.ImageField(
        required=False,  # Make it optional
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            UserProfile.objects.create(user=user, avatar=self.cleaned_data.get('avatar'))
        return user

class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select Category",
        required=True,
        widget=forms.Select(attrs={'class': 'form-select', 'aria-label': 'Category'})
    )
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter post title',
        'aria-label': 'Post Title'
    }))
    subtitle = forms.CharField(
        max_length=300,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter a subtitle (optional)',
            'aria-label': 'Subtitle'
        })
    )
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 4,
        'placeholder': 'Enter post content...',
        'aria-label': 'Post Content'
    }))
    url = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter external URL (optional)',
            'aria-label': 'External URL'
        })
    )
    featured_image = forms.ImageField(
        required=False,
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
                'rows': 4,
                'style': 'max-height: 150px; overflow-y: auto;',
            }),
        }
