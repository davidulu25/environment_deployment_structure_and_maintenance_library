from django.urls import path
from . import views

urlpatterns = [
    path('singular', views.BookSingularView.as_view(), name='book_singular'),
    path('list', views.BookListView.as_view(), name='book_list'),
]