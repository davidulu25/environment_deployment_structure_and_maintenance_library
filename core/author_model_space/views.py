import os
import environ

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

from rest_framework import generics, authentication, permissions
from rest_framework.response import Response

from .models import Author
from .serializers import AuthorSerializer

env = environ.Env()
env.read_env("../")

class AuthorSingularView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    if env("ENVIRONMENT") == "production":
        authentication_classes = [authentication.BasicAuthentication]
        permission_classes = [permissions.IsAuthenticated]
    else:
        authentication_classes = []
        permission_classes = []
    

    def get_object(self):
        author_id = self.request.query_params.get("id")
        author = Author.objects.get(id=author_id)
        return author
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 60 * 2))
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

class AuthorListView(generics.ListAPIView, generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # function to override deleting single model instance
    def destroy(self, request, *args, **kwargs):
        queryset = Author.objects.all()
        respite, _ = queryset.delete()
        return Response({"message": f"all author profiles ({respite}) were deleted"})

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