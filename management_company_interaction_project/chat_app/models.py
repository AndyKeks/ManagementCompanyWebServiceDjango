from django.db import models

from requests_app.models import Request


class RequestMessage(models.Model):
    STATUS_CHOICES = [
        ('отправлено', 'отправлено'),
        ('доставлено', 'доставлено'),
    ]
    request = models.ForeignKey(Request, on_delete=models.CASCADE, verbose_name='Заявка')
    is_system = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='Статус сообщения')
    content = models.CharField(max_length=500, verbose_name='Контент')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата, время отправки сообщения')

    def __str__(self):
        return self.content


class Attachment(models.Model):
    message = models.ForeignKey(RequestMessage, on_delete=models.CASCADE)
    file = models.FileField(upload_to="images/requests/attachment_message/", blank=True, null=True)
