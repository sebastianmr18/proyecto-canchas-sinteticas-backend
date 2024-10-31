from django.db import models
from .user_model import User
from .court_model import Court

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('Confirmado', 'Confirmado'),
        ('Cancelado', 'Cancelado'),
        ('Completado', 'Completado'),
    ]

    reservation_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(auto_now_add=True)
    start_datetime = models.DateTimeField()
    duration_hours = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Confirmado')
    is_notified = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Reservación'
        verbose_name_plural = 'Reservaciones'

    def __str__(self):
        return f'Reservación {self.reservation_id} - {self.user.first_name} {self.user.last_name} ({self.email}) en {self.court.location}'