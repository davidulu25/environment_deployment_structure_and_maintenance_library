from django.urls import path
from . import views

urlpatterns = [
    path('singular', views.TaskSingularView.as_view(), name='task_singular'),
        path('list', views.TaskListView.as_view(), name='task_list'),
]