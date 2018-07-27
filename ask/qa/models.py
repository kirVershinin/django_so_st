from django.contrib.auth.models import User
from django.db import models

class QuestionManager(models.Manager):
	def new():
		return self.order_by('-added_at')
	def popular():
		return self.order_by('-rating')


class Question(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default = 0)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	likes = models.ManyToManyField(User, related_name='likes_set')
	objects = QuestionManager()		
	
	def __str__ (self):
		return self.text	


class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__ (self):
   		return self.text
	




	
