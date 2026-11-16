from json import JSONDecodeError

from django.db.models import Model
from django.http import HttpResponse, JsonResponse
import json
from urllib import request

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt



from scrum.models import Tarea, Sprint, Programador, Etiqueta


def bienvenida(Request):
    return HttpResponse("Jeffrey Epstein voy a por ti")

def listar_tareas(request):
    if request.method != "GET":
        return JsonResponse("Metodo equivocado")

    tareas = Tarea.objects.all().values()

    return JsonResponse( list(tareas), safe=False)

def listar_tarea(request, id):
    if request.method != "GET":
        return JsonResponse("Metodo equivocado")
    tarea = Tarea.objects.get(id=id)
    datos = {
        "id" : tarea.id,
        "nombre" : tarea.nombre,
        "fecha_inicio" : {
            tarea.fecha_inicio.isoformat()
            if tarea.fecha_inicio else None
        },
        "fecha_fin" : {
            tarea.fecha_fin.isoformat()
            if tarea.fecha_fin else None
        },
        "completa" : tarea.completada,
        "sprint_id": tarea.sprint,
        "programador_id" : tarea.programador
    }
    return JsonResponse(list(datos), safe=False)

def listar_tarea_mejorado(request, id):
    if request.method != "GET":
        return JsonResponse("Metodo equivocado")

    tarea = Tarea.objects.filter(id=id).values().first()

    return JsonResponse(tarea)

def listar_tareas_completas(request):
    if request.method != "GET":
        return JsonResponse("Metodo equivocado")
    tareas = Tarea.objects.filter().values()
    tareas_completadas = tareas.filter(completada=True)
    return JsonResponse(list(tareas_completadas), safe=False)



def validar_tarea(tareaJson):
    error = []
    sprint_id = tareaJson.get("sprint_id")
    if sprint_id and not Sprint.objects.filter(id=sprint_id).exists():
        error.append("El sprint no existe")

    programador_id = tareaJson.get("programador_id")
    if programador_id and not Programador.objects.filter(id=programador_id).exists():
        error.append("El id del programador no existe")

    return error


def crear_etiquetas(etiquetas, objeto):
    if isinstance(objeto, Tarea):
        for etiqueta in etiquetas:
            etiqueta_model, creada = Etiqueta.objects.get_or_create(nombre=etiqueta)
            objeto.etiqueta.add(etiqueta_model)
            if creada:
                print("Se ha creado la etiqueta")
            else:
                print("etiqueta nueva")
    elif isinstance(objeto, Programador):
        for etiqueta in etiquetas:
            etiqueta_model, creada = Etiqueta.objects.get_or_create(nombre=etiqueta)
            objeto.etiquetas.add(etiqueta_model)
            if creada:
                print("Se ha creado la etiqueta")
            else:
                print("etiqueta nueva")




@csrf_exempt
def crear_tareas(request):
    if request.method != "POST":
        return JsonResponse(data={"error": "Error esta petición solo funciona con post"}, status=405)

    try:
        tarea_json = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse(data={"error": "Json no está bien formado"}, status=400)

    # Validar relaciones
    errores = validar_tarea(tarea_json)
    if errores:
        return JsonResponse(data={"errores": errores}, status=400)

    # Aquí hacemos el post protegido con su propio try-except
    try:
        tarea = Tarea.objects.create(
            nombre=tarea_json.get("nombre"),
            fecha_inicio=tarea_json.get("fecha_inicio"),
            fecha_fin=tarea_json.get("fecha_fin"),
            completada=tarea_json.get("completada", False),
            sprint_id=tarea_json.get("sprint_id"),
            programador_id=tarea_json.get("programador_id"),
        )
        etiquetas = tarea_json.get("etiquetas", [])
        crear_etiquetas(etiquetas, tarea)


        return JsonResponse({
            "exito": "Se ha creado la tarea correctamente",
            "tarea": tarea.nombre
        }, status=201)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)



@csrf_exempt
def crear_programador(request):
    if request.method != "POST":
        return JsonResponse(data={"error": "Error esta petición solo funciona con post"}, status=405)

    try:
        programador_json = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse(data={"error": "Json no está bien formado"}, status=400)

    programador = Programador.objects.create(
        nombre = programador_json.get("nombre"),
        apellido1 = programador_json.get("apellido1")
    )
    etiquetas = programador_json.get("etiquetas", [])
    crear_etiquetas(etiquetas, programador)

    return JsonResponse({
        "exito": "Se ha creado la tarea correctamente",
        "programador": programador.nombre
    }, status=201)
