from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication

from rest_framework.response import Response

@api_view()
def index(request):
    """
    PURPOSE:
    friendly landing page for execution of logout action
    """
    return HttpResponse("welcome; login <a href='http://localhost:8000/auth/login'>here</a>", headers={
        "content-type": "text/html"
    })

@api_view()
@authentication_classes([BasicAuthentication])
def login_view(request):
    """
    PURPOSE:
    logs in a user to sign in once and access other views without repeatedly signing in
    """
    login(request, request.user)
    return Response("Sign in succesful!")

@api_view()
def logout_view(request):
    """
    PURPOSE:
    signs a user out and sets user object in request to Anonymous
    """
    logout(request)
    return redirect("index")