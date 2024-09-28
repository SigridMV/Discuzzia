from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Route for the home page
    path('create/', views.create_topic, name='create_topic'),  # Route to create a new topic
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),  # Route to view topic details
    path('forum/', views.forum, name='forum'),  # Route to the forum page
    path('moderation/', views.moderation, name='moderation'),  # Route for moderation
    path('edit_topic/<int:topic_id>/', views.edit_topic, name='edit_topic'),  # Route to edit a topic
    path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic'),  # Route to delete a topic
    path('edit_reply/<int:reply_id>/', views.edit_reply, name='edit_reply'),  # Route to edit a reply
    path('delete_reply/<int:reply_id>/', views.delete_reply, name='delete_reply'),  # Route to delete a reply
    
]
