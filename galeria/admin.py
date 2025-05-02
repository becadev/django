from django.contrib import admin
from galeria.models import Fotografia
# Register your models here.

# configurações do django admin para melhorar a visualização
class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id",  "nome", "legenda")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria",)

admin.site.register(Fotografia, ListandoFotografias)