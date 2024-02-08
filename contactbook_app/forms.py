from django import forms
from django.core.exceptions import ValidationError
from .models import User
from django.contrib.auth.password_validation import validate_password

class RegistrationForm(forms.ModelForm):
  username = forms.CharField(label='名前')
  phone_number = forms.CharField(max_length=15, label='電話番号', required=False)
  home_address = forms.CharField(max_length=100, label='住所', required=False)
  email = forms.EmailField(label='メールアドレス')
  password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
  reenter_password = forms.CharField(label='パスワード（確認用）', widget=forms.PasswordInput())

  class Meta():
    model = User
    fields = ('username', 'phone_number', 'home_address', 'email', 'password')

  def clean_email(self):
    email = self.cleaned_data.get('email')
    if User.objects.filter(email=email).exists():
      raise ValidationError('同じメールアドレスの登録があります。')
    return email


  def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data['password']
    reenter_password = cleaned_data['reenter_password']
    if password != reenter_password:
      raise forms.ValidationError('パスワードが異なります。もう一度試してください')

  def save(self, commit=False):
    r_user = super().save(commit=False)
    validate_password(self.cleaned_data['password'], r_user)
    r_user.set_password(self.cleaned_data['password'])
    r_user.save()
    return r_user
  
class LoginForm(forms.Form): 
  email = forms.EmailField(label="メールアドレス")
  password = forms.CharField(label="パスワード", widget=forms.PasswordInput())

class UserEditForm(forms.ModelForm): 
  username = forms.CharField(label='名前')
  phone_number = forms.CharField(max_length=15, label='電話番号', required=False)
  home_address = forms.CharField(max_length=100, label='住所', required=False)
  email = forms.EmailField(label='メールアドレス')

  class Meta:
    model = User
    fields = ('username', 'phone_number', 'home_address', 'email')

class ChangePasswordForm(forms.ModelForm): 
    
  password = forms.CharField(label='新しいパスワード', widget=forms.PasswordInput())
  reenter_password = forms.CharField(label='新しいパスワード（確認用）', widget=forms.PasswordInput())

  class Meta():
    model = User
    fields = ('password',)

  def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data['password']
    reenter_password = cleaned_data['reenter_password']
    if password != reenter_password:
      raise forms.ValidationError('Password is different. Please try again')

  def save(self, commit=False):
    r_user = super().save(commit=False)
    validate_password(self.cleaned_data['password'], r_user)
    r_user.set_password(self.cleaned_data['password'])
    r_user.save()
    return r_user