from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# ders1

# def home_page(request):
#     return HttpResponse("Home")

# def about_page(request):
#     return HttpResponse("About")

def about_details(request):
    return HttpResponse("Details")

# ders2
def home_page(request):
    return render(request, "index.html")

def about_page(request):
    return render(request, "about/about.html")  