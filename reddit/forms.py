from django import forms
from .models import Post, Category  

class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select Category",
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'category']  

    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select a Category")        
