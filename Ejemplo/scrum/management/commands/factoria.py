import random

import faker.providers.date_time
from django.core.management import BaseCommand, color
from django.db.models import Model
from faker import Faker
from ...models import Tarea, Etiqueta, Programador, Sprint, Proyecto

class Command(BaseCommand):
    help = "Factoria"

    def handle(self, *args, **options):
            try:
                fake = Faker()
                for i in range(1):
                    proyecto = Proyecto(nombre=fake.user_name())
                    proyecto.save()
                    self.stdout.write(self.style.SUCCESS(f"el proyecto {proyecto.nombre} se ha insertado correctamente"))

                for i in range(4):
                    sprint = Sprint(fecha_inicio = fake.date_time(), fecha_fin= fake.date_time())
                    sprint.save()
                    self.stdout.write(self.style.SUCCESS(f"el sprint se ha insertado correctamente"))


                for i in range (10):
                    ##CREACION DE PROGRAMADOR
                    programador = Programador(nombre=fake.name(), apellido1=fake.last_name())
                    programador.save()
                    self.stdout.write(self.style.SUCCESS(
                        f"El programador {programador.nombre}, {programador.apellido1} se ha insertado correctamente"))
                for i in range(30):
                    ##CREACION DE TAREA
                    tareas = Tarea.objects.all()
                    programadores = Programador.objects.all()
                    sprints = Sprint.objects.all()
                    proyectos = Proyecto.objects.all()

                    sprints.proyecto = proyectos
                    tarea = Tarea(nombre=random.choice(tareas), programador= random.choice(programadores),sprint=random.choice(sprints))
                    tarea.save()
                    self.stdout.write(self.style.SUCCESS(f"la tarea con nombre {tarea.nombre} se ha insertado correctamente"))

            except BaseException as e:
                self.stdout.write(self.style.SUCCESS(f"Se ha producido un fallo al crear la tarea{e}"))