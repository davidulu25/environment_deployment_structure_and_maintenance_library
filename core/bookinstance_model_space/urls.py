from django.urls import path
from . import views

urlpatterns = [
    path('singular', views.BookInstanceSingularView.as_view(), name='bookinstance_singular'),
    path('list', views.BookInstanceListView.as_view(), name='bookinstance_list'),
]