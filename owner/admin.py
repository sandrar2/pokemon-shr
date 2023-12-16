from django.contrib import admin
from .models import Owner


#admin.site.register(Owner)
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'edad')
    list_filter = ('edad', 'pais')
    search_fields = ('nombre', 'pais')
    #fields = ('edad', 'pais', 'nombre')
