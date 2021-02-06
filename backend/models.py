from django.db import models
from django.contrib.auth.models import User


class OpencvUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="static/images/opencv_users/")

    def __str__(self):
        return str(self.user.username)
    
    class Meta:
        verbose_name = "Фото пользователя"
        verbose_name_plural = "Фото пользователей"
