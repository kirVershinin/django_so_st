from django import forms
from django.forms import ModelForm, HiddenInput, PasswordInput
from .models import Question, Answer, User
from django.contrib.auth import authenticate, login

class AskForm(ModelForm):
	class Meta:
		model = Question
		fields = ['title','text', 'author']
		widgets = {'author':HiddenInput}

class AnswerForm(ModelForm):
	class Meta:
		model = Answer
		fields = ['text','question','author']
		widgets = {'question':HiddenInput, 'author':HiddenInput}

class SignUpForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password']
		widget = {'password':PasswordInput}

class LoginForm(forms.Form):
	username = forms.CharField(max_length=255)
	password = forms.CharField(widget=forms.PasswordInput) 

