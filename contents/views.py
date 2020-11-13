from django.shortcuts import render, redirect

# Create your views here.
def about(request):
    return render(request, "about.html")

def team(request):
    return render(request, "contact.html")

def model(request):
    return render(request, "model.html")