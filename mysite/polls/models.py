from django.db import models
from django.db.models import CharField
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> str:
        return str(self.question_text)

    def was_published_recently(self) -> str:
        return str(self.pub_date) >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        verbose_name = 'Вопросы'
        verbose_name_plural = "Вопросы"



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def str(self) -> str:
        return f'question: {self.question}/n' \
               f'choice_text: {self.choice_text}/n' \
               f'votes: {self.votes}'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = "Ответы"