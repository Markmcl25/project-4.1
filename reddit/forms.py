from django import forms
from .models import Post, Category  

class PostForm(forms.ModelForm):
    # Define the category field with a custom widget
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select Category",  # Placeholder text for the dropdown
        required=True,
        widget=forms.Select(attrs={'class': 'form-select', 'aria-label': 'Category'})
    )
    
    # Define the title field with a custom widget and placeholder
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter post title', 
            'aria-label': 'Post Title'
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

    class Meta:
        model = Post
        fields = ['title', 'content', 'category']
