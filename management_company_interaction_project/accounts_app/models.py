from django.contrib.auth.models import User
from django.db import models


class OrganisationProfile(models.Model):
    representative = models.OneToOneField(User, on_delete=models.CASCADE,
                                          verbose_name='Представитель/руководитель организации')
    name = models.CharField(max_length=100, verbose_name='Наименование организации')
    address = models.CharField(max_length=100, verbose_name='Адрес организации')

    phone_number = models.CharField(max_length=17,
                                    verbose_name='Номер телефона для связи')

    def __str__(self):
        return self.name
