from re import template
from django.urls import path
from .views import (
    CardListView, 
    CardCreateView, 
    CardUpdateView
)

urlpatterns = [
    path("", CardListView.as_view(), name="card-list"),
    path('new', CardCreateView.as_view(), name="card-create"),
    path("edit/<int:pk>/", CardUpdateView.as_view(), name="card-update")
]