import datetime  # Step 2.7
# Step 2.2 'manage.py migrate'
# Step 2.5 'manage,py makemigrations polls' then '... migrate'

from django.db import models  # Step 2.3
from django.utils import timezone  # Step 2.7
# Create your models here.


class Question(models.Model):  # Step 2.3
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):  # Step 2.6
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):  # Step 2.3
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):  # Step 2.6
        return self.choice_text
