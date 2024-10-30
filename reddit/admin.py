from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    search_fields = ('title', 'content', 'slug')  # Add search functionality
    ordering = ('-created_on',)  # Orders by created_on in descending order
    summernote_fields = ('content',)  # Corrected this line

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on', 'post')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments', 'disapprove_comments']
    ordering = ('-created_on',)  # Orders by created_on in descending order
    date_hierarchy = 'created_on'  # Add date hierarchy for filtering


    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = "Approve selected comments"

    def disapprove_comments(self, request, queryset):
        queryset.update(approved=False)
    disapprove_comments.short_description = "Disapprove selected comments"