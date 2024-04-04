from django.shortcuts import render

from rest_framework import generics, authentication, permissions
from rest_framework.response import Response

from .models import Genre
from .serializers import GenreSerializer

from django.http import HttpResponse
from django.core.cache import cache

class GenreSingularView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        genre_id = self.request.query_params.get("id")
        genre = Genre.objects.get(id=genre_id)
        return genre
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if self.request.query_params.get("id"):
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.create(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        if self.request.query_params.get("id"):
            return self.update(request, *args, **kwargs)
        else:
            return self.create(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        if self.request.query_params.get("id"):
            return self.destroy(request, *args, **kwargs)
        else:
            return self.create(request, *args, **kwargs)

class GenreListView(generics.ListAPIView, generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # function to override deleting single model instance
    def destroy(self, request, *args, **kwargs):
        queryset = Genre.objects.all()
        respite, _ = queryset.delete()
        return Response({"message": f"all genres ({respite}) were deleted successfully"})

    def get(self, request, *args, **kwargs):
        if self.get_queryset() is None:
            return self.create(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        if self.get_queryset() is None:
            return self.create(request, *args, **kwargs)
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        if self.get_queryset() is None:
            return self.create(request, *args, **kwargs)
        return self.destroy(request, *args, **kwargs)