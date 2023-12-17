from django.shortcuts import render
from .models import Owner


# Create your views here.

def owner_list(request):
    peru_owners = Owner.objects.filter(pais='Peru')

    hardcoded_data = [
        {
            'nombre': 'Maria Fernandez',
            'edad': 15,
            'pais': 'Peru',
            'dni': 12345678,
            'vigente': False,
            'pokemons': [
                {'nombre_pokemon': 'Charizar',
                 'ataques': ['Ataque 1 - Charizard', 'Ataque 2 - Charizard', 'Ataque 3 - Charizard']

                 }

            ]
        },
        {
            'nombre': 'Mario Ramirez',
            'edad': 25,
            'pais': 'Brasil',
            'dni': 12389730,
            'vigente': True
        },
        {
            'nombre': 'Juan Hernandez',
            'edad': 35,
            'pais': 'Peru',
            'dni': 77777777,
            'vigente': False
        }
    ]

    database_data = [
        {
            'nombre': owner.nombre,
            'edad': owner.edad,
            'pais': owner.pais,
            'dni': owner.dni,
            'vigente': owner.vigente
        }
        for owner in peru_owners
    ]

    data_context = hardcoded_data + database_data

    return render(request, 'owner_list.html', context={'data': data_context})
