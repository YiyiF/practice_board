from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('practices/', views.PracticeListView.practice_list_view, name='practices'),
    path('practices/<pk>/', views.PracticeDetailView.as_view(), name='practice-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/<slug>/', views.AuthorDetailView.as_view(), name='author-detail'),
]