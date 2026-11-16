from django.db import models

# Create your models here.
class Etiqueta(models.Model):
    nombre  = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Programador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    etiquetas = models.ManyToManyField(Etiqueta, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido1}"


class Proyecto(models.Model):
    nombre  = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Sprint(models.Model):
    fecha_inicio = models.DateField(blank=True, null= True)
    fecha_fin = models.DateField(blank=True, null= True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, blank=True, null= True)



class Tarea(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_inicio = models.DateField(blank=True, null= True)
    fecha_fin = models.DateField(blank=True, null= True)
    completada = models.BooleanField(default=False)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, blank=True, null= True)
    programador = models.ForeignKey(Programador, on_delete=models.CASCADE, blank=True, null= True)
    etiqueta = models.ManyToManyField(Etiqueta,  blank=True)

    def __str__(self):
        return f"[{self.nombre}]" + ", ".join([e.nombre for e in self.etiqueta.all()])

