from django.urls import path
from . import views

app_name = 'board_app'

urlpatterns = [
  path('create_topic', views.create_topic, name='create_topic'),
  path('list_topics', views.list_topics, name='list_topics'),
  path('edit_topic/<int:id>', views.edit_topic, name='edit_topic'),
  path('delete_topic/<int:id>', views.delete_topic, name='delete_topic'),
  path('post_texts/<int:topic_id>', views.post_texts, name='post_texts'),
  path('password_required/<int:topic_id>/', views.password_required, name='password_required'),
]