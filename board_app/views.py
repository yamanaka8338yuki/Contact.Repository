
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from django.contrib import messages
from .models import Topics, Texts
from django.http import Http404

def create_topic(request):
  create_topic_form = forms.CreateTopicForm(request.POST or None)
  if create_topic_form.is_valid():
    create_topic_form.instance.user = request.user
    create_topic_form.save()
    messages.success(request, 'ボードが作成されました')
    return redirect('board_app:list_topics')
  return render(
    request, 'board_app/create_topic.html', context={
      'create_topic_form': create_topic_form,
    }
  )

def list_topics(request): 
  topics = Topics.objects.pick_all_topics()
  return render(
    request, 'board_app/list_topics.html', context={
      'topics': topics
    }
  )

def edit_topic(request, id): 
  topic = get_object_or_404(Topics, id=id)
  if topic.user.id != request.user.id:
    raise Http404
  edit_topic_form = forms.CreateTopicForm(request.POST or None, instance=topic)
  if edit_topic_form.is_valid():
    edit_topic_form.save()
    messages.success(request, 'ボードが更新されました')
    return redirect('board_app:list_topics')
  return render(
    request, 'board_app/edit_topic.html', context={
      'edit_topic_form': edit_topic_form,
      'id': id,
    }
  )

def delete_topic(request, id): 
  topic = get_object_or_404(Topics, id=id)
  if topic.user.id != request.user.id:
    raise Http404
  delete_topic_form = forms.DeleteTopicForm(request.POST or None)
  if delete_topic_form.is_valid():
    topic.delete()
    messages.success(request, 'ボードが削除されました')
    return redirect('board_app:list_topics')
  return render(
    request, 'board_app/delete_topic.html', context={
      'delete_topic_form': delete_topic_form
    }
  )

@login_required
def post_texts(request, topic_id):
    # 認証済みの情報を取得
    auth_topic_id = request.session.get('board_auth_topic_id')

    if auth_topic_id != topic_id:
        # 認証されていない場合はログインパスワード画面にリダイレクト
        return redirect('board_app:password_required', topic_id=topic_id)

    post_text_form = forms.PostTextForm(request.POST or None)
    topic = get_object_or_404(Topics, id=topic_id)
    texts = Texts.objects.pick_by_topic_id(topic_id)

    if post_text_form.is_valid():
        post_text_form.instance.topic = topic
        post_text_form.instance.user = request.user
        post_text_form.save()
        return redirect('board_app:post_texts', topic_id=topic_id)

    return render(
        request, 'board_app/post_texts.html', context={
            'post_text_form': post_text_form,
            'topic': topic,
            'texts': texts,
        }
    )


@login_required
def password_required(request, topic_id):
    topic = get_object_or_404(Topics, id=topic_id)

    if request.method == 'POST':
        password_form = forms.PasswordForm(request.POST)

        if password_form.is_valid() and topic.user.check_password(password_form.cleaned_data['password']):
            # パスワードが認証されたらセッションに認証済みの情報を保存
            request.session['board_auth_topic_id'] = topic.id
            return redirect('board_app:post_texts', topic_id=topic_id)
        else:
            messages.error(request, 'パスワードが間違っています')

    else:
        password_form = forms.PasswordForm()

    return render(
        request, 'board_app/password_required.html', context={
            'password_form': password_form,
            'topic': topic,
        }
    )