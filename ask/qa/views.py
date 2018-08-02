from django.http import HttpResponseRedirect
from .models import Question, Answer
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import AskForm, AnswerForm


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
			post=form.save()
			return HttpResponseRedirect(reverse('question', args=[post.question.id]))
	else:
		form = AnswerForm(initial={'question':str(question_id)})
	return render(request, 'question.html',{'user':request.user, 'question':question, 'form':form})


def ask(request):
	if request.method == 'POST':
		form = AskForm(request.POST)
		if form.is_valid():
			post=form.save()
			return HttpResponseRedirect(reverse('question', args=[post.id]))
	else:
		form = AskForm()
	return render(request, 'ask_add.html', {'form':form})

