from django.http import HttpResponseRedirect, HttpResponse
from .models import Question, Answer, User
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import AskForm, AnswerForm, SignUpForm, LoginForm

def latest(request):
	qu_list = Question.objects.all().order_by('-added_at')
	paginator = Paginator(qu_list, 10)
	page = request.GET.get('page')
	question = paginator.get_page(page)	
	return render(request, 'latest.html', {'question':question})
						
def popular(request):
	pop_list = Question.objects.all().order_by('-rating')
	paginator = Paginator(pop_list, 10)
	page = request.GET.get('page')
	question = paginator.get_page(page)
	return render(request, 'popular.html', {'question':question})

def question(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	if request.method == 'POST':
		form = AnswerForm(request.POST)
		if form.is_valid():
			form._user = request.user 
			post = form.save()
			return HttpResponseRedirect(reverse('question', args=[post.question.id]))
	else:
		form = AnswerForm(initial={'question':str(question_id),'author':request.user})
	return render(request, 'question.html',{'user':request.user, 'question':question, 'form':form})

def ask(request):
	if request.method == 'POST':
		form = AskForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return HttpResponseRedirect(reverse('question', args=[post.id]))
	else:
		form = AskForm(initial={'author':request.user})
	return render(request, 'ask_add.html', {'form':form, 'user':request.user})

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			email = form.cleaned_data.get("email")
			password = form.cleaned_data.get("password")
			user = User.objects.create_user(username,email,password)
			if user is not None:
				login(request,user)
				return HttpResponseRedirect('/')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form':form})	

def loginx(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)	
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			user = authenticate(request, username=username, password=password)
			if user is not None:
				logout(request)
				login(request, user)
				return HttpResponseRedirect('/')
	else:
		form = LoginForm()	
	return render(request, 'login.html', {'form':form})


