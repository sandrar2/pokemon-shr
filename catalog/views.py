from django.shortcuts import render


# Create your views here.

def catalog_list(request):
    data_context = {
        'nombre': 'Katty Paredes',

    }

    return render(request, 'catalog_list.html', context={'data': data_context})
