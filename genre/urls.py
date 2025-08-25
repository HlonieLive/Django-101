from django.urls import path
from . import views

urlpatterns = [
    # Genre page
    path('', views.genre.as_view(), name="genre"),
    # Details page
    path('<pk>/', views.details.as_view(), name='details'),
    
    path('register/', views.UserFormView.as_view(), name='admin'),
]
