from django.urls import path
from . import views

app_name = 'letter_app'

urlpatterns = [
    path('letter_list/', views.letter_list, name='letter_list'),
    path('view_file/<int:file_id>/', views.view_file, name='view_file'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('delete_file/<int:file_id>/', views.delete_file, name='delete_file'),
]