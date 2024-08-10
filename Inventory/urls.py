from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='homepage'),
    path('about/', views.AboutPage, name='about'),
    path('blog/', views.BlogPage, name='blog'),
    path('faq/', views.FaqPage, name='faq'),
    path('special/', views.SpecialPage, name='special'),
    path('raga/add/', views.RagaAdd, name='raga_add'),
    path('ragas/', views.AllRagas, name='raga_list'),
    path('raga/<int:id>/', views.raga_detail, name='raga_detail'),
]
