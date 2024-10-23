from django.db import models
from .user_model import User

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'

    def __str__(self):
        return f'Administrador: {self.user.first_name} {self.user.last_name}'