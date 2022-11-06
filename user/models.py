from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resim = models.FileField(upload_to="profil resimleri/", verbose_name="Hesabım Resmi")
    tel = models.IntegerField()

    def __str__(self):
        return self.user.username