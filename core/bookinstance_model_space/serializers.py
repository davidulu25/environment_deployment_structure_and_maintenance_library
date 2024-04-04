from rest_framework import serializers

from .models import BookInstance
from book_model_space.serializers import BookSerializer

class BookInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields = ["book", "imprint", "id", "due_back", "status", "borrower"]