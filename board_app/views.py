
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
    if request.user.auth == 'admin':
        # 特権ユーザー（保育士）の場合は全てのボードを表示
        topics = Topics.objects.pick_all_topics()
    else:
        # 一般ユーザー（保護者）の場合は自分が作成したボードのみ表示
        topics = Topics.objects.filter(user=request.user)

    return render(
        request, 'board_app/list_topics.html', context={
            'topics': topics
        }
    )

def edit_topic(request, id): 
    topic = get_object_or_404(Topics, id=id)

    # 特権ユーザー（admin）はどのボードでも編集可能
    if request.user.auth != 'admin' and topic.user.id != request.user.id:
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

    # 特権ユーザー（admin）はどのボードでも削除可能
    if request.user.auth != 'admin' and topic.user.id != request.user.id:
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

