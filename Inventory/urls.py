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
    path('raga/raga--<str:name>/', views.raga_detail, name='raga_detail'),
    path('songs/', views.AllSongs, name='song_list'),
    path('song/song--<str:name>/', views.song_detail, name='song_detail'),
    path('varnams/', views.AllVarnams, name='varnam_list'),
    path('varnam/varnam--<str:name>/', views.varnam_detail, name='varnam_detail'),
    path('comparisons/', views.AllComparisons, name='comparison_list'),
    path('diy/', views.AllDoItYourself, name='diy_list'),
    path('diy/diy--<str:name>/', views.diy_detail, name='diy_detail'),
]