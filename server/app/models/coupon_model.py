from django.db import models
from .user_model import User

class Coupon(models.Model):
    coupon_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    used = models.BooleanField(default=False)    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cupón'
        verbose_name_plural = 'Cupones'

    def __str__(self):
        return f'Cupón {self.coupon_id} de {self.discount}% perteneciente a {self.user.first_name}'