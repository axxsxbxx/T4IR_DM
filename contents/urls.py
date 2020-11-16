from django.urls import path
from . import views

urlpatterns =[
    path('about/', views.about, name="about"),
    path('team/', views.team, name="team"),
    path('model/', views.model, name="model"),
    path('group1/', views.group1, name="group1"),
    path('group2/', views.group2, name="group2"),
    path('group3/', views.group3, name="group3"),
    path('group4/', views.group4, name="group4"),
    path('randomforest/', views.randomforest, name="randomforest"),
    path('knn/', views.knn, name="knn"),
    path('logistic/', views.logistic, name="logistic"),
    path('ada/', views.ada, name="ada"),
    path('xgb/', views.xgb, name="xgb"),
    path('model/', views.model, name="model"),

]