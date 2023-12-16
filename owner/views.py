from django.shortcuts import render

# Create your views here.

def owner_list(request):

    data_context = {
        'nombre': 'Katty Paredes',
        'edad': 20,
        'dni': '12345678',
        'pais': 'Peru',
        'vigente': False,
    }

    return render(request,'owner_list.html', context={'data': data_context})



