from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Expense(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    month = models.CharField(max_length=255)

    def __str__(self):
        return self.title
