from django.db import models
from .user_model import User

class Notification(models.Model):        
    TYPE_CHOICES = [
        ('reservación', 'Reservación'),
        ('promoción', 'Promoción'),
        ('pago', 'Pago'),
        ('review', 'Review'),
        ('other', 'Other'),
    ]

    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    title = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Notificación'
        verbose_name_plural = 'Notificaciones'

    def __str__(self):
        return f'Notification para {self.user.first_name} {self.user.last_name} ({self.user.email}): {self.title}'