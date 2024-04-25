
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('todo/',views.todoapi.as_view(),name="books")
]
