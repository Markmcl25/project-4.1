from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField
import uuid

# Status options for the post status field
STATUS = ((0, "Draft"), (1, "Published"))

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)  # Allow blank initially
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reddit_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    url = models.URLField(max_length=500, blank=True, null=True)  # New URL field
    # Add a default category (make sure to replace `1` with the appropriate category ID)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    upvotes = models.ManyToManyField(User, related_name='upvoted_posts', blank=True)
    downvotes = models.ManyToManyField(User, related_name='downvoted_posts', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def total_votes(self):
        return self.upvotes.count() - self.downvotes.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            # Automatically generate a slug if it doesn't exist
            self.slug = slugify(self.title) + "-" + str(uuid.uuid4())[:8]  # Unique slug with title + UUID
        super().save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)  # Added approved field here

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"