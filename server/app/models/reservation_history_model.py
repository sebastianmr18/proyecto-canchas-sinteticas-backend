from django.db import models
from .user_model import User
from .court_model import Court

class ReservationHistory(models.Model):
    STATUS_CHOICES = [
        ('Confirmado', 'Confirmado'),
        ('Cancelado', 'Cancelado'),
        ('Completado', 'Completado'),
    ]
    reservation_history_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    date = models.DateTimeField()
    duration = models.DurationField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Confirmado')

    class Meta:
        verbose_name = 'Historial de Reserva'
        verbose_name_plural = 'Historiales de Reserva'

    def __str__(self):
        return f"Reserva {self.status} por {self.user.email} en {self.cancha.location}"
