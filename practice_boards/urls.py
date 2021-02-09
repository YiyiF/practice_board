from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('practices/', views.PracticeListView.as_view(), name='practices'),
    path('practices/<pk>/', views.PracticeDetailView.as_view(), name='practice-detail'),
]