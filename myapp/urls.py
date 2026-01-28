from django.urls import path
from .views import CocaColaApiView
urlpatterns = [
    path('cola/',CocaColaApiView.as_view()),
    path('cola/<int:pk>/', CocaColaApiView.as_view()),
]

