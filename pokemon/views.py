from django.shortcuts import render

# Create your views here.

def pokemon_list(request):

    data_context = {
        'Nombre': 'Katty Paredes',
        'Numero': 20,
        'Generacion': '12345678',
        'Tipo': 'Peru',

    }

    return render(request,'owner_list.html', context={'data': data_context})