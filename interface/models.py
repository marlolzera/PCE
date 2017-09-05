from django.db import models
from django.contrib.auth.models import User


class UsuarioInfo(models.Model):
    user = models.OneToOneField(User)
    endereco = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username
