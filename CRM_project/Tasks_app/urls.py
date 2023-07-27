
from django.urls import path
from .views import *   

urlpatterns = [
    path('taskspost', CreateTasks.as_view(), name='taskpost'),
   
]
