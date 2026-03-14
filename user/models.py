from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Register_user(models.Model):
    username = models.CharField(max_length = 100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)