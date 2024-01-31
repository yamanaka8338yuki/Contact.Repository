from django import forms
from .models import UploadedFile

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['title', 'file']
        labels = {
            'title': 'タイトル',
            'file': 'ファイル',
        }
