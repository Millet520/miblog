from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True, blank=False)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', blank=True)
    user_desc = models.CharField(max_length=500, blank=True)

    class Meta:
        db_table = 'tb_users'
        verbose_name = 'usermanage'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.mobile
