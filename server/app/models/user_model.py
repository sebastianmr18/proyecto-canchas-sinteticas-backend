from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from ..managers import UserManager
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.validators import RegexValidator

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
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],
        blank=True, null=True
    )
    address = models.CharField(
        'Dirección', max_length=100, blank=True, null=True)
    
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='cliente')

    date_register = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField('Usuario Activo', default=True)

    is_staff = models.BooleanField('Usuario parte del Staff', default=False)    

    is_superuser = models.BooleanField('Superusuario', default=False)
    
    profile_picture = models.ImageField(upload_to='profile_picture/', blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_id','first_name', 'last_name']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.email} - {self.first_name} {self.last_name}'
    
    def get_email(self):
        return self.email
    
    def get_user_id(self):
        return self.user_id
    
    def get_first_name(self):
        return self.first_name
    
    def get_middle_name(self):
        return self.middle_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_second_last_name(self):
        return self.second_last_name
    
    def get_contact_number(self):
        return self.contact_number
    
    def get_address(self):
        return self.address
    
    def get_rol(self):
        return self.rol
    
    def get_date_register(self):
        return self.date_register
    
    def get_is_active(self):
        return self.is_active
    
    def get_is_staff(self):
        return self.is_staff
    
    def get_is_superuser(self):
        return self.is_superuser
    
    def get_profile_picture(self):
        return self.profile_picture