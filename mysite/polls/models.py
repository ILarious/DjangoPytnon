from django.db import models
from django.db.models import CharField
import datetime
from django.utils import timezone



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> CharField:
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'\nquestion: {self.question}\n' \
               f'choice_text: {self.choice_text}\n' \
               f'votes: {self.votes}'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'