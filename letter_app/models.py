from django.db import models
from django.contrib.auth.models import User

class UploadedFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploaded_files/')
    uploaded_by = models.ForeignKey('contactbook_app.User', on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

        