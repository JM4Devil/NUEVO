from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from core.models import Doctor
# Create your views here.
def home(request):
    data ={
        'title' : 'App Medica',
        'description': 'Esta es una pagina web',
        'author': 'Gary',
        'year': 2025,
    }
    doctores = Doctor.objects.all()
    data["doctores"]=doctores
    #return JsonResponse({"mesage": "hello world"})
    return render(request, 'home.html',  data)
