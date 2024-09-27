from django import forms
from .models import Topic, Reply, Post

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'content'] # Fields for creating a new topic

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content'] # Field for creating a new reply

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']  # Field for creating a new post
