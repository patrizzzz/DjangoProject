from django.contrib.auth.models import User
from django.db import models



# Create your models here.
class category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    budget_limit = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)