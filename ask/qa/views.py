from django.http import HttpResponse
from .models import Question, Answer
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

def latest(request):
	qu_list = Question.objects.all().order_by('-added_at')
	paginator = Paginator(qu_list, 10)
	page = request.GET.get('page')
	question = paginator.get_page(page)	
	return render(request, 'latest.html', {
		'question':question})
							
def popular(request):
	pop_list = Question.objects.all().order_by('-rating')
	paginator = Paginator(pop_list, 10)
	page = request.GET.get('page')
	question = paginator.get_page(page)
	return render(request, 'popular.html', {
		'question':question})

def question(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	answer = Answer.objects.all()
	return render(request, 'question.html', {
		'question':question})
