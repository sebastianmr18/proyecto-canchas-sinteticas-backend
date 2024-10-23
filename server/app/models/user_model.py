from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from ..managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    ROL_CHOICES = [
        ('cliente', 'Cliente'),
        ('administrador', 'Administrador'),
    ]
    
    user_id = models.CharField('Número de Identificación',primary_key=True, unique=True)

    email = models.EmailField(
        'Correo Electrónico', unique=True)
    
    first_name = models.CharField(
        'Primer Nombre', max_length=30)

    middle_name = models.CharField(
        'Segundo Nombre', max_length=30, blank=True, null=True)

    last_name = models.CharField('Primer Apellido', max_length=30)

    second_last_name = models.CharField(
        'Segundo Apellido', max_length=30, blank=True, null=True)
    
    contact_number = models.CharField(
        'Teléfono de Contacto', max_length=15, blank=True, null=True)

    address = models.CharField(
        'Dirección', max_length=100, blank=True, null=True)
    
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='cliente')

    date_register = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField('Usuario Activo', default=True)

    is_staff = models.BooleanField('Usuario parte del Staff', default=False)    

    is_superuser = models.BooleanField('Superusuario', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_id','first_name', 'last_name']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.email} - {self.first_name} {self.last_name}'