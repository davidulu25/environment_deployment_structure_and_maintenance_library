from django.shortcuts import render
from django.utils.decorators import method_decorator

from rest_framework import generics, authentication, permissions
from rest_framework.response import Response

from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

from .models import Book
from .serializers import BookSerializer

import environ

env = environ.Env()
env.read_env("../")

class BookSingularView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        book_id = self.request.query_params.get("id")
        book = Book.objects.get(id=book_id)
        return book
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if self.request.query_params.get("id"):
            return self.retrieve(request, *args, **kwargs)
        return self.create(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        if self.request.query_params.get("id"):
            return self.update(request, *args, **kwargs)
        return self.create(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        if self.request.query_params.get("id"):
            return self.destroy(request, *args, **kwargs)
        return self.create(request, *args, **kwargs)

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # def create(self, request, *args, **kwargs):
    #     obj_data = request.data.get("")
    #     pass

    # only work on update and not create
    def update(self, request, *args, **kwargs):
        pass
    
    @method_decorator(cache_page(60 * 60 * 2.5))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    if env("ENVIRONMENT") != "production":
        def destroy(self, request, *args, **kwargs):
            queryset = Book.objects.all()
            respite, _ = queryset.delete()
            return Response({"message": f"all tasks ({respite}) were deleted successfully"})

    
    def get(self, request, *args, **kwargs):
        if self.get_queryset() is None:
            return self.create(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        db_params = dict(request.query_params.iterlists())
        
        if self.get_queryset() is None:
            return self.create(request, *args, **kwargs)
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        if self.get_queryset() is None:
            return self.create(request, *args, **kwargs)
        return self.destroy(request, *args, **kwargs)