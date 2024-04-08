"""
URL configuration for environment_deployment_structure_and_maintenance_library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication_view_space.urls')),
    path('books/', include('book_model_space.urls')),
    path('authors/', include('author_model_space.urls')),
    path('bookinstances/', include('bookinstance_model_space.urls')),
    path('genres/', include('genre_model_space.urls')),
    # path('count/', include('count_view_space.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('tasks/', include('task_model_space.urls')),
]