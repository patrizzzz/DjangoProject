from django.db import models
from django.contrib.auth.models import User


class RecurringtransacConfig(models.Model):
    Choices_cat= [
        ('loans','Loans'),
        ('entertainment','Entertainment'),
        ('investment','Investment'),('health','Health'),
        ('sports,','Sports'),
    ]


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(choices=Choices_cat, max_length=50)
    frequency = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()




# Create your models here.
