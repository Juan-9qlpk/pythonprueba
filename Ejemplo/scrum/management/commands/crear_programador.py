from django.core.management import BaseCommand, color
from django.db.models import Model
from ...models import Programador

class Command(BaseCommand):
    help = "Este comando va a crear programadores de verdad"

    def handle(self, *args, **options):


        try:
            programador = Programador(nombre="Juan", apellido1="Delgado")
            programador.save()
            self.stdout.write(self.style.SUCCESS(f"El programador {programador.nombre}, {programador.apellido1} se ha insertado correctamente"))

        except BaseException as e:
            self.stdout.write(self.style.SUCCESS(f"Se ha producido un fallo al crear el programador{e}"))