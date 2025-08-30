from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.thought_list, name = "thought_list"),
    path('thought_list/', views.thought_list, name = "thought_list"),
    path('create/', views.thought_create, name = "thought_create"),
    path('<int:thought_id>/edit/', views.thought_edit, name = "thought_edit"),
    path('<int:thought_id>/delete/', views.thought_delete, name = "thought_delete"),
    path('register', views.register, name = "register"),
]
