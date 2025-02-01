from django.urls import path
from . import views

urlpatterns = [
    path("", views.recipes, name="recipes"),  # Homepage ("/")
    path("details/<int:id>/", views.details, name="details"),  # Details page
    path("courses", views.courses, name="courses"),  # courses page
    path("thoughts", views.thoughts, name="thoughts"),  # thoughts page
]