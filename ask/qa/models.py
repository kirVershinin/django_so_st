from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='question_author')
	likes = models.ManyToManyField(User, related_name='question_likes')


class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now=True)
	question = models.ForeignKey(Question, blank=True, null=True, on_delete=models.CASCADE)
	author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='answer_author')

	def __str__ (self):
		return self.text
