from django.urls import path
from . import views

urlpatterns = [
    path('', views.latest, name='latest'),
	path('signup/', views.signup, name='signup'),
	path('login/', views.loginx, name='login'),
	path('ask/', views.ask, name='ask'),
	path('popular/', views.popular, name='popular'),
	path('question/<question_id>/', views.question, name='question'),
]
