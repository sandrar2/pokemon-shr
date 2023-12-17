from django.shortcuts import render
from .models import Owner
# Create your views here.

def owner_list(request):
    peru_owners = Owner.objects.filter(pais='Peru')
    data_context = {
        'nombre': 'Maria',
        'edad': 15,
        'pais': 'Peru'
    }
    return render(request, 'owner_list.html', context={'data': data_context})








