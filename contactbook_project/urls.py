from django.contrib import admin
from django.urls import path, include 
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
  path('admin/', admin.site.urls),
  path('contactbook_app/', include('contactbook_app.urls')), 
  path('board_app/', include('board_app.urls')),
  path('letter_app/', include('letter_app.urls')),
  path('event_app/', include('event_app.urls')),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)