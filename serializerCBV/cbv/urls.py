from django.urls import path
from cbv.views import *

urlpatterns = [
    path('students/', StudentList.as_view()),
    path('students/<int:pk>/', StudentDetail.as_view()),
]