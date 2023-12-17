from django.shortcuts import render


# Create your views here.

def pokemon_list(request):
    data_context = {
        'nombre': 'Maria',
        'edad': 15,
        'pais': 'Argentina'
    }

    if data_context['edad'] >= 18:
        data_context['mensaje'] = 'Maria es mayor de edad'
    else:
        data_context['mensaje'] = 'Maria es menor de edad'

    return render(request, 'pokemon_list.html', context={'data': data_context})




