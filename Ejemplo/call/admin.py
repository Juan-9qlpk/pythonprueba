from django.contrib import admin

from .models import Persona
from .models import Jugador

# Register your models here.
admin.site.register(Persona)
admin.site.register(Jugador)