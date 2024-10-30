from django.contrib import admin
from .models import Post
from .models import Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    search_fields = ('title', 'content', 'slug') # Add search functionality
    ordering = ('-created_on',) # Orders by created_on in descending order
    summernot_fields = ('content',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on', 'post')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments', 'disapprove_comments']
    ordering = ('-created_on',)  # Orders by created_on in descending order
    date_hierarchy = 'created_on'  # Add date hierarchy for filtering
    approved = models.BooleanField(default=False)
    



