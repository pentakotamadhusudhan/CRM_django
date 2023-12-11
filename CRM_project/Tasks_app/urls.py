
from django.urls import path
from .views import *   
from .curd.task import CreateTasks
from .curd.taskbyid import TaskById


urlpatterns = [
    path('taskspost', CreateTasks.as_view(), name='taskpost'),
    path('taskbyid/<int:id>', TaskById.as_view(), name='task')
   
]
