from django.shortcuts import render
from .models import Pokemon

# Create your views here.

def pokemon_list(request):
    fire_pokemons = Pokemon.objects.filter(Tipo='fuego')
    data_context = {
        'Nombre': 'charmander',
        'Generacion': 'segunda',
        'Tipo': 'fuego'
    }

    return render(request, 'pokemon_list.html', context={'data': data_context})





