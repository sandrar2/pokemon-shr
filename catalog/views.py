from django.shortcuts import render


# Create your views here.

def catalog_list(request):
    data_context = {
        'nombre': 'Luis',
        'edad': 25,
        'pais': 'Peru'
    }

    if data_context['edad'] >= 18:
        data_context['mensaje'] = 'Luis es mayor de edad'
    else:
        data_context['mensaje'] = 'Luis es menor de edad'

    return render(request, 'catalog_list.html', context={'data': data_context})




