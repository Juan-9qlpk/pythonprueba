from django.core.management import BaseCommand, color
from django.db.models import Model
from ...models import Programador, Tarea

class Command(BaseCommand):
    help = "Este comando va a crear programadores de verdad"

    def handle(self, *args, **options):
        programador = Programador.objects.get(pk=1)
        tarea = Tarea(nombre="judiada historica monumental (recoger centimos del suelo)", programador=programador)
        tarea.save()
        self.stdout.write(self.style.SUCCESS(
            f"Listar tarea con programador existente"))