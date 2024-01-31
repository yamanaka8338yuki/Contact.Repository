from django import forms
from .models import Topics, Texts

class CreateTopicForm(forms.ModelForm):
  title = forms.CharField(label='タイトル')

  class Meta:
    model = Topics
    fields = ('title',)

class DeleteTopicForm(forms.ModelForm): 

  class Meta:
    model = Topics
    fields = []

class PostTextForm(forms.ModelForm): 
  text = forms.CharField(
    label='', 
    widget=forms.Textarea(attrs={
      'rows':10,
      'cols':50
      })
    )
    
  class Meta:
    model = Texts
    fields = ('text',)

class PasswordForm(forms.Form):
    password = forms.CharField(label='ボード作成者のパスワードを入力してください。', widget=forms.PasswordInput)