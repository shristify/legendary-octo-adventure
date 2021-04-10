from django.urls import path
from . import views
from .views import HomeView
urlpatterns = [
    path('', HomeView, name='home'),
    path('sendsms/', views.sendsms, name='sendsms'),
    path('doctorsnearme/', views.DocsNear, name='maps'),
    path('quiz/', views.quiz, name='quiz'),
    path('you/', views.you, name='you'),
   
]
