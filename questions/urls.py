from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='question-list'),        # GET & POST
    path('<int:id>/', views.question_detail, name='question-detail'),  # GET, PUT, DELETE
]
