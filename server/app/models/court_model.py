from django.db import models

class Court(models.Model):
    SURFACE_TYPE_CHOICES = [
        ('pasto', 'Pasto'),
        ('arena', 'Arena'),
        ('otro', 'Otro'),
    ]

    court_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    surface_type = models.CharField(max_length=20, choices=SURFACE_TYPE_CHOICES)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    capacity = models.IntegerField()

    class Meta:
        verbose_name = 'Cancha'
        verbose_name_plural = 'Canchas'

    def __str__(self):
        return f'Cancha {self.court_id} - {self.name}'