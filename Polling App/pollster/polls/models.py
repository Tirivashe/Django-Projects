from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField('Date Published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #this field is related to the question by use of Foreign Key and models.CASCADE makes sure if the parent class is deleted, the child is deleted too
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text