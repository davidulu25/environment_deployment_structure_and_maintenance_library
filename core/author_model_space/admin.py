from django.contrib import admin

from .models import Author
from book_model_space.admin import BooksInline

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    
    inlines = [BooksInline]