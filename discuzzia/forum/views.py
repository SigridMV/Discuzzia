from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Reply
from .forms import TopicForm, ReplyForm
from django.contrib.auth import logout

@login_required
def moderation(request):
    if not request.user.is_staff:  # Check if the user is an admin
        return redirect('index')  # Redirect to the home page if not admin

    topics = Topic.objects.all()  # Get all topics
    replies = Reply.objects.all()  # Get all replies
    return render(request, 'forum/moderation.html', {'topics': topics, 'replies': replies})

@login_required
def edit_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)

    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return redirect('moderation')  # Redirect back to moderation
    else:
        form = TopicForm(instance=topic)

    return render(request, 'forum/edit_topic.html', {'form': form})

@login_required
def delete_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method == 'POST':
        topic.delete()
        return redirect('moderation')  # Redirect back to moderation
    return render(request, 'forum/confirm_delete_topic.html', {'topic': topic})

@login_required
def edit_reply(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id)

    if request.method == 'POST':
        form = ReplyForm(request.POST, instance=reply)
        if form.is_valid():
            form.save()
            return redirect('moderation')  # Redirect back to moderation
    else:
        form = ReplyForm(instance=reply)

    return render(request, 'forum/edit_reply.html', {'form': form})

@login_required
def delete_reply(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id)
    
    if not request.user.is_staff:  # Only admins can delete replies
        return redirect('index')
    
    if request.method == 'POST':
        reply.delete()
        return redirect('moderation')  # Redirect back to moderation
    return render(request, 'forum/confirm_delete_reply.html', {'reply': reply})


def index(request):
    return render(request, 'forum/index.html')  # Render the 'index.html' template

@login_required
def forum(request):
    topics = Topic.objects.all().order_by('-created_at')  # Get all topics ordered by creation date
    return render(request, 'forum/forum.html', {'topics': topics})


@login_required
def create_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.author = request.user  # Assign the current user as the author
            topic.save()
            return redirect('topic_detail', topic_id=topic.id)
    else:
        form = TopicForm()
    return render(request, 'forum/create_topic.html', {'form': form})

@login_required
def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    replies = topic.replies.all()
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.author = request.user
            reply.topic = topic
            reply.save()
            return redirect('topic_detail', topic_id=topic.id)
    else:
        form = ReplyForm()
    return render(request, 'forum/topic_detail.html', {'topic': topic, 'replies': replies, 'form': form})


@login_required
def delete_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    
    if not request.user.is_staff:  # Only admins can delete
        return redirect('index')  # Non-admins are redirected
    
    if request.method == 'POST':
        topic.delete()
        return redirect('moderation')  # Redirect back to moderation
    return render(request, 'forum/confirm_delete_topic.html', {'topic': topic})


# def custom_logout(request):
#     logout(request) 
#     return redirect('index')
