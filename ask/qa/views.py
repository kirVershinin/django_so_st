from django.http import HttpResponse
from .models import Question, Answer
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

def latest(request):
	qu_list = Question.objects.all().order_by('new')
	paginator = Paginator(qu_list, 10)
	page = request.GET.get('page')
	question = paginator.get_page(page)	
	return render(request, 'latest.html', {
		'question': question})
							
def popular(request):
	pop_list = Question.objects.all().order_by('popular')
	paginator = Paginator(pop_list, 10)
	page = request.GET.get('page')
	popular = paginator.get_page(page)
	return render(request, 'popular.html', {
		'popular':popular})

def question(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	answer = Answer.objects.all()
	return render(request, 'qa/question.html', {
		'question':question,
		'answer': answer,
	})
