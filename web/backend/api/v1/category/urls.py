from django.urls import path

from .views import (
    CategoryDestroyView, CategoryCreateView
)


urlpatterns = [
    path("", CategoryCreateView.as_view()),
    path("<int:pk>", CategoryDestroyView.as_view())
]