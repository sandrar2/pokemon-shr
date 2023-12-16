from django.shortcuts import render

def pokemon_list(request):
    data_context = {
        'Nombre': 'Katty Paredes',
        'Numero': 20,
        'Generacion': '12345678',
        'Tipo': '',
    }

    # Corrige el nombre de la plantilla a 'pokemon_list.html'
    return render(request, 'pokemon_list.html', context={'data': data_context})


