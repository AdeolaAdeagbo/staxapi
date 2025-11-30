from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course-list'),       # GET & POST
    path('<int:id>/', views.course_detail, name='course-detail'),  # GET, PUT, DELETE
]
