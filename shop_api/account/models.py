from django.db import models

# Create your models here.
#
from django.contrib.auth.models import AbstractUser
import uuid
from .manager import UserManager

class CustomUser (AbstractUser):
    email = models.EmailField(unique= True)#это поле будет уникальным
    username = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)#blank=True - это означает что поля не обязательно
    is_active = models.BooleanField(default=False)#это поле азначает что активен или нет
    activation_code = models.CharField(max_length=300, blank=True)

    objects = UserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []#обязательные поля

    def create_activation_code(self):
        code = str(uuid.uuid4())#тут генерирует рандомное выражение для активации
        self.activation_code = code
        self.save()



