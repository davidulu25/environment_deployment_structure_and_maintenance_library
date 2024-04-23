from django.shortcuts import render

from rest_framework import generics, authentication, permissions
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer

import environ

env = environ.Env()
env.read_env("../../.env")

class TaskSingularView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        task_id = self.request.query_params.get("id")
        task = Task.objects.get(id=task_id)
        return task
    
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

class TaskListView(generics.ListAPIView, generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # function to override deleting single model instance
    if env("CONTEXT") != "production":
        def destroy(self, request, *args, **kwargs):
            queryset = Task.objects.all()
            respite, _ = queryset.delete()
            return Response({"message": f"all tasks ({respite}) were deleted successfully"})


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