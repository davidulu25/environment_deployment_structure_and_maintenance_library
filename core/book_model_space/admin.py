from django.contrib import admin

from .models import Book
from bookinstance_model_space.admin import BooksInstanceInline

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BooksInstanceInline]

class BooksInline(admin.TabularInline):
    model = Book
    extra = 0