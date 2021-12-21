from django.core import validators
from django.db import models

from accounts_app.models import OrganisationProfile


class Request(models.Model):
    TYPE_REQUESTS_CHOICES = [
        ('Электрика', 'Электрика'),
        ('Сантехника', 'Сантехника'),
        ('Вентиляция', 'Вентиляция'),
        ('Связь и наблюдение', 'Связь и наблюдение'),
        ('Плотнические работы', 'Плотнические работы'),
    ]
    STATUS_CHOICES = [
        ('На рассмотрении', 'На рассмотрении'),
        ('В работе', 'В работе'),
        ('Закрыта', 'Закрыта'),
    ]
    type = models.CharField(max_length=30, verbose_name='Тип заявки', choices=TYPE_REQUESTS_CHOICES)
    title = models.CharField(max_length=100, verbose_name='Краткое описание проблемы')
    description = models.TextField(verbose_name='Подробности проблемы')
    number_office = models.CharField(verbose_name='Номер офиса', max_length=5)
    image = models.ImageField(verbose_name='Фото проблемы', upload_to="images/requests/main_pictures/",
                              validators=[validators.validate_image_file_extension])
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время заявки')
    account = models.ForeignKey(OrganisationProfile, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, default='На рассмотрении', verbose_name='Статус заявки',
                              max_length=25)

    def __str__(self):
        return f'{self.id}: {self.title}'


