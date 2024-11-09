from django.contrib import admin
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django_summernote.admin import SummernoteModelAdmin

# Register Post model with Summernote and additional configurations
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    search_fields = ('title', 'content', 'slug')  # Add search functionality
    ordering = ('-created_on',)  # Orders by created_on in descending order
    summernote_fields = ('content',)  # This will enable Summernote on 'content' field

# Register Comment model with additional configurations
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on', 'post')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments', 'disapprove_comments', 'delete_comments']  # Add delete action
    ordering = ('-created_on',)  # Orders by created_on in descending order
    date_hierarchy = 'created_on'  # Add date hierarchy for filtering

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = "Approve selected comments"

    def disapprove_comments(self, request, queryset):
        queryset.update(approved=False)
    disapprove_comments.short_description = "Disapprove selected comments"
    
    # Custom action to delete selected comments
    def delete_comments(self, request, queryset):
        queryset.delete()
    delete_comments.short_description = "Delete selected comments"

# Customize the UserAdmin to display additional fields
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name')

# Unregister the default User model and register it with CustomUserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
