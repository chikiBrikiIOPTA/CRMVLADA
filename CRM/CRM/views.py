from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "index.html")

def main(request):
    return render(request, "Главная.html")

def music(request):
    return render(request, "Музыка.html")

def contact(request):
    return render(request, "Контакты.html")

def about(request):
    return render(request, "О-нас.html")

def track1(request):
    return render(request, "Трек1.html")

def track2(request):
    return render(request, "Трек2.html")

def track3(request):
    return render(request, "Трек3.html")

def track4(request):
    return render(request, "Трек4.html")