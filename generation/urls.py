from django.urls import path, include
from . import views

urlpatterns = [
path('generate', views.GeneratedStringListCreate.as_view()),
]
