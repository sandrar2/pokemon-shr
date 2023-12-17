from django.contrib import admin
from .models import Pokemon


class PokemonAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Generacion', 'Tipo')
    list_editable = ('Tipo',)
    search_fields = ('Nombre',)
    exclude = ('Generacion',)


def get_fields(self, request, obj=None):
    return ('Nombre', 'Generacion', 'Tipo')

admin.site.register(Pokemon, PokemonAdmin)






