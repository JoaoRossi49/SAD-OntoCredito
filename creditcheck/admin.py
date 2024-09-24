from django.contrib import admin
from .models import *


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'salario', 'nivel_escolar','quantidade_cartoes', 'dividas', 'saldo')

admin.site.register(Cliente, ClienteAdmin)