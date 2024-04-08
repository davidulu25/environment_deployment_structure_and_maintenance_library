from django.shortcuts import render

from rest_framework import generics, authentication, permissions
from rest_framework.response import Response

from .models import BookInstance
from .serializers import BookInstanceSerializer

import environ

env = environ.Env()
env.read_env("../")

class BookInstanceSingularView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        bookinstance_id = self.request.query_params.get("id")
        bookinstance = BookInstance.objects.get(id=bookinstance_id)
        return bookinstance
    
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

class BookInstanceListView(generics.ListAPIView, generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer
    authentication_classes = [authentication.BasicAuthentication]
    if env("ENVIRONMENT") == "development":
        permission_classes = [permissions.IsAuthenticated]
    else:
        permission_classes = [permissions.IsAdminUser]

    # function to override deleting single model instance
    if env("ENVIRONMENT") != "production":
        def destroy(self, request, *args, **kwargs):
            queryset = BookInstance.objects.all()
            respite, _ = queryset.delete()
            return Response({"message": f"all bookinstances ({respite}) were deleted successfully"})
        

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