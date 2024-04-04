from django.urls import path
from . import views

urlpatterns = [
    path('singular', views.AuthorSingularView.as_view(), name='author_singular'),
    path('list', views.AuthorListView.as_view(), name='author_list'),
]