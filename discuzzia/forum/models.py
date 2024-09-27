from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    title = models.CharField(max_length=200)  # Title of the topic
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # User who created the topic
    content = models.TextField()  # Content of the topic
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the topic was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the topic was last updated

    def __str__(self):
        return self.title  # Returns the title of the topic

class Reply(models.Model):
    topic = models.ForeignKey(Topic, related_name='replies', on_delete=models.CASCADE)  # Topic to which the reply belongs
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # User who wrote the reply
    content = models.TextField()  # Content of the reply
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the reply was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the reply was last updated

    def __str__(self):
        return f'Reply by {self.author} on {self.topic}'  # Returns a string representation of the reply

class Post(models.Model):  
    title = models.CharField(max_length=200)  # Title of the post
    content = models.TextField()  # Content of the post
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the post was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the post was last updated
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # User who created the post

    def __str__(self):
        return self.title  # Returns the title of the post
