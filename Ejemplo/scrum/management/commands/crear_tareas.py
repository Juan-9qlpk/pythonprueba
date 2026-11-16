from django.core.management import BaseCommand, color
from django.db.models import Model
from ...models import Tarea, Etiqueta, Programador

class Command(BaseCommand):
    help = "Este comando va a crear tareas de prueba"

    def handle(self, *args, **options):


        try:
            ##CREACION DE ETIQUETA
            etiqueta = Etiqueta(nombre="Siervo de Jeffrey Epstein")
            etiqueta.save()
            self.stdout.write(self.style.SUCCESS(f"la etiqueta {etiqueta.nombre} se ha insertado correctamente"))


            ##CREACION DE PROGRAMADOR
            programador = Programador(nombre="Juan", apellido1="Delgado")
            programador.save()
            self.stdout.write(self.style.SUCCESS(
                f"El programador {programador.nombre}, {programador.apellido1} se ha insertado correctamente"))

            ##CREACION DE TAREA
            tarea = Tarea(nombre="judiada historica monumental (recoger centimos del suelo)", programador= programador)
            tarea.save()
            tarea.etiqueta.add(etiqueta)


            self.stdout.write(self.style.SUCCESS(f"la tarea con nombre {tarea.nombre} se ha insertado correctamente"))
        except BaseException as e:
            self.stdout.write(self.style.SUCCESS(f"Se ha producido un fallo al crear la tarea{e}"))