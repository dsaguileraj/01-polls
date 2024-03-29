from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('post/', views.post_question, name='post_question'),
    path('create-choice/', views.create_choice, name='create_choice'),
    path('delete/<int:question_id>', views.delete_question, name='delete_question'),
]

