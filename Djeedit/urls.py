"""Djeedit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
import django.contrib.auth.urls
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mainPage, name="home"),
    path('topic/<str:topicName>/', views.topicPage, name="topic"),
    path('topic/<str:topicName>/post/<int:postID>/', views.postPage, name="post"),
    path('topic/<str:topicName>/create_post/', views.createPost, name="create_post"),
    path('topic_create/', views.createTopic, name="topic_create"),
    path('login/', django.contrib.auth.views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout',  auth_views.LogoutView.as_view(next_page='/'), name="logout"),
    path('navbarsearch', views.navbarSearch, name="navbarSearch"),
    re_path(r'^search$', views.search, name="search")
]
