from django.core.management import BaseCommand, color
from django.db.models import Model
from ...models import Tarea

class Command(BaseCommand):
    help = ""

    def handle(self, *args, **options):

        tareas = Tarea.objects.all()

        for tarea in tareas:
            print(f"{tarea.id} {tarea.nombre}")

        self.stdout.write(self.style.SUCCESS("Este comando lista todas las tareas"))