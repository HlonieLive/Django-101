from django.urls import path
from . import views

urlpatterns = [
    # Genre page
    path("genre/", views.genre, name="genre"),
    
    # Genre 1
    path("<int:genre_id", views.details, name="details"),
]
