from django import forms
from .models import Post, Category  

class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select Category",  # Placeholder text for the dropdown
        required=True,
        widget=forms.Select(attrs={'class': 'form-select', 'aria-label': 'Category'})
    )
    
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter post title', 'aria-label': 'Post Title'})
    )

    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter post content...', 'aria-label': 'Post Content'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'category']

    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Post Title'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your post content here...'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all())