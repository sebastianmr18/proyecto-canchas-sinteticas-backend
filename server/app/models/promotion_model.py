from django.db import models
from .court_model import Court

class Promotion(models.Model):
    promotion_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Promoción'
        verbose_name_plural = 'Promociones'

    def __str__(self):
        return f'Promoción {self.promotion_id} de {self.discount}% en {self.court.location}'