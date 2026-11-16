from django.db.models import Model
from django.test import TestCase
from .models import Tarea, Etiqueta, Sprint, Programador
from datetime import date

class TareaTest(TestCase):


    def setUp(self):
        self.programador = Programador.objects.create(
            nombre="Francisco"
        )

        self.sprint = Sprint.objects.create(
            fecha_inicio=date(2026,11,9)
        )

    def test_crear_tarea_api(self):
        datos = {
            "nombre": "Desarrollar el login",
            "fecha_inicio": "2026-10-28",
            "fecha_fin": None,
            "completa": False,
            "sprint_id": self.sprint.id,
            "programador_id": self.programador.id,
            "etiquetas": ["Backend", "SQL"]
        }

        respuesta = self.client.post(
            "/tareas/crear/",
            data=datos,
            content_type="application/json"
        )

        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(Tarea.objects.count(), 1)
        
    def test_num_sprint(self):
        sprint = Sprint.objects.all()
        self.assertCountEqual(len(sprint), 1)

    def test_suma(self):
        resultado = 4 + 4
        self.assertEqual(resultado, 8)


    def test_resta(self):
        resultado = 10-5
        self.assertEqual(resultado, 5)

    def test_comparacion(self):
        comprobacion = True
        nombre = "Francisco"
        nombre2 = "francisco"
        if nombre != nombre2:
            comprobacion = False

        self.assertTrue(comprobacion)