from django.db import models

class TopicsManager(models.Manager): 

  def pick_all_topics(self):
    return self.order_by('id').all()

class Topics(models.Model):

  title = models.CharField(max_length=100)
  user = models.ForeignKey(
    'contactbook_app.User', on_delete=models.CASCADE
  )

  objects = TopicsManager() 

  class Meta:
    db_table = 'topics'

class TextsManager(models.Manager):
  def pick_by_topic_id(self, topic_id):
    return self.filter(topic_id=topic_id).order_by('id').all()

class Texts(models.Model):

  text = models.CharField(max_length=500)
  user = models.ForeignKey(
    'contactbook_app.User', on_delete=models.CASCADE
  )
  topic = models.ForeignKey(
    'Topics', on_delete=models.CASCADE
  )

  objects = TextsManager()

  class Meta:
    db_table = 'texts'