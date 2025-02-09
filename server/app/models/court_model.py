from django.db import models

class Court(models.Model):
    SURFACE_TYPE_CHOICES = [
        ('pasto', 'Pasto'),
        ('arena', 'Arena'),
        ('arcilla', 'Arcilla'),
        ('ladrillo', 'Ladrillo'),
        ('otro', 'Otro'),
    ]

    SPORT_CHOICES = [
        ('futbol', 'Futbol'),
        ('tenis', 'Tenis'),
        ('voleibol', 'Voleibol'),
        ('otro', 'Otro'),
    ]

    court_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    surface_type = models.CharField(max_length=20, choices=SURFACE_TYPE_CHOICES, default='otro')
    sport = models.CharField(max_length=20, choices=SPORT_CHOICES, default='otro')
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    capacity = models.IntegerField()
    has_active_promotion = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Cancha'
        verbose_name_plural = 'Canchas'

    def __str__(self):
        return f'Cancha {self.court_id} - {self.name}'
    
class CourtImage(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='court_images/')

    class Meta:
        verbose_name = 'Imagen de Cancha'
        verbose_name_plural = 'Imagenes de Canchas'