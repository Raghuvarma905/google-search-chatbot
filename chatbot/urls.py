from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),              # home page - chat UI
    path('search/', views.get_results), # search endpoint
]
