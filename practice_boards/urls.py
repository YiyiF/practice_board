from django.urls import path
# from django.conf.urls import url
from . import views, submit_practice
# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('practices/', views.PracticeListView.practice_list_view, name='practices'),
    path('practices/<pk>/', views.PracticeDetailView.as_view(), name='practice-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/<slug>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('submit/', views.SubmitPracticeView.as_view(), name='submit'),
]