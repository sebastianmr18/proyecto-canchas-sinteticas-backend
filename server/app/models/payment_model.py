from django.db import models
from .reservation_model import Reservation
from .coupon_model import Coupon

class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('Exitoso', 'Exitoso'),
        ('Pendiente', 'Pendiente'),
        ('Fallido', 'Fallido'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('tarjeta', 'Tarjeta'),
        ('efectivo', 'Efectivo'),
        ('otro', 'Otro'),
    ]
    
    payment_id = models.AutoField(primary_key=True)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='tarjeta')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Exitoso')
    is_confirmed = models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'

    def __str__(self):
        return f'Pago {self.payment_id} - Reservación {self.reservation.reservation_id} - Confirmado: {self.is_confirmed}'