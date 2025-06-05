from django.db import models

# Create your models here.
class AsadoAudit(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    adultos_completa = models.PositiveIntegerField()
    adultos_moderada = models.PositiveIntegerField()
    ninos = models.PositiveIntegerField()
    vegetarianos = models.PositiveIntegerField()
    cortes = models.CharField(max_length=255, blank=True)
    generoso = models.BooleanField(default=False)
    incluir_acompanamientos = models.BooleanField(default=False)
    solo_picada = models.BooleanField(default=False)
    incluir_bebidas = models.BooleanField(default=False)
    resultado = models.JSONField()  # Guarda el resultado completo para análisis
    ip = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    referer = models.TextField(blank=True)
    usuario = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Asado {self.fecha} - {self.adultos_completa} adultos"
