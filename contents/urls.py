from django.urls import path
from . import views

urlpatterns =[
    path('about/', views.about, name="about"),
    path('team/', views.team, name="team"),
    path('model/', views.model, name="model"),
]