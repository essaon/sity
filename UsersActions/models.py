from django.db import models


class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    publish_date = models.DateField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question_text = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
