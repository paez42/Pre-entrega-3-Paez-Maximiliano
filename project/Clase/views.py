from django.shortcuts import render

from . import models
# Create your views here.

def home(request):
    query = models.Comision.objects.all()
    context = {"comisiones":query}
    return render(request, "Clase/index.html", context)