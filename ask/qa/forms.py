from django.forms import ModelForm, HiddenInput
from .models import Question, Answer


class AskForm(ModelForm):
	class Meta:
		model = Question
		fields = ['title','text']


class AnswerForm(ModelForm):
	class Meta:
		model = Answer
		fields = ['text','question']
		widgets = {'question':HiddenInput}
