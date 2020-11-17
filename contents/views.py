from django.shortcuts import render, redirect

# Create your views here.
def about(request):
    return render(request, "about.html")

def team(request):
    return render(request, "contact.html")

def model(request):
    return render(request, "model.html")

def group1(request):
    return render(request, "group1.html")

def group2(request):
    return render(request, "group2.html")

def group3(request):
    return render(request, "group3.html")

def group4(request):
    return render(request, "group4.html")

def randomforest(request):
    return render(request, "randomforest.html")

def knn(request):
    return render(request, "knn.html")

def logistic(request):
    return render(request, "logistic.html")

def ada(request):
    return render(request, "ada.html")

def xgb(request):
    return render(request, "xgb.html")

def model(request):
    return render(request, "model.html")