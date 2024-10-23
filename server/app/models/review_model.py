from django.db import models
from .user_model import User
from .court_model import Court

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Rating from 1 to 5
    comment = models.TextField(blank=True, null=True)
    review_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f'Review {self.review_id} - {self.user.first_name} {self.user.last_name}'