from django.contrib import admin
from .models import Contato
# Register your models here.

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'criado_em')
    search_fields = ('nome', 'email')