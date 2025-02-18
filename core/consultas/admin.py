from django.contrib import admin

from .models import Consulta, Medico, Paciente

admin.site.register(Consulta)
admin.site.register(Medico)
admin.site.register(Paciente)