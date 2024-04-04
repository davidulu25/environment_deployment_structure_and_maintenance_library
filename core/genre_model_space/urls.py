from django.urls import path
from . import views

urlpatterns = [
    path('singular', views.GenreSingularView.as_view(), name='genre_singular'),
    path('list', views.GenreListView.as_view(), name='genre_list'),
]