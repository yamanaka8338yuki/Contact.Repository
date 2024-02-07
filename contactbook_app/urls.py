from django.urls import path
from . import views

app_name = 'contactbook_app'

urlpatterns = [
  path('', views.home, name='home'),
  path('registration', views.registration, name='registration'),
  path('login_page', views.login_page, name='login_page'), 
  path('logout_page', views.logout_page, name='logout_page'),
  path('edit_page', views.edit_page, name='edit_page'), 
  path('change_password', views.change_password, name='change_password'),
]