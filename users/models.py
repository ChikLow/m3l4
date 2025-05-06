from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=524, unique=True)
    role = models.CharField(max_length=50, choices=[("admin", "admin"),("user", "user")], default='user')