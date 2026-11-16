from django.urls import path
from . import views
from django.urls import path, include

from django.urls import path
from . import views

urlpatterns = [
    path("crearTarea", views.crear_tareas, name="crear_tarea"),
    path("crearProgramador", views.crear_programador, name="crear_programador"),
    path("bienvenida/", views.bienvenida, name="bienvenida"),
    path("listarTareas/", views.listar_tareas, name="listarTareas"),
    path("listarTarea/<int:id>", views.listar_tarea, name="listarTarea"),
    path("listarTareaMejorada/<int:id>", views.listar_tarea_mejorado, name="listarTareaMejorada"),
    path("listarTareasCompletas/", views.listar_tareas_completas, name="listarTareasCompletas"),
]