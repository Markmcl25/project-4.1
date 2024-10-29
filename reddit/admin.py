from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    search_fields = ('title', 'content', 'slug') # Add search functionality
    ordering = ('-created_on',) # Orders by created_on in descending order
    summernot_fields = ('content')


