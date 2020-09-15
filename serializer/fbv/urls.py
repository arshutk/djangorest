from django.urls import path
from fbv.views import *

urlpatterns = [
    path('students/', student_list),
    path('students/<int:pk>/', student_detail),
]