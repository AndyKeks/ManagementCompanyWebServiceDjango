from PIL import Image
from django import forms
from django.forms import ModelForm

from requests_app.constants import IMAGE_HELP_TEXT, MIN_RESOLUTION_IMAGE, MAX_RESOLUTION_IMAGE, MAX_SIZE_BYTES_IMAGE
from requests_app.models import Request


class NewRequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ('type', 'title', 'description', 'number_office', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = IMAGE_HELP_TEXT

    def clean(self):
        cleaned_data = super(NewRequestForm, self).clean()

        image = cleaned_data.get('image')

        if image is None:
            raise forms.ValidationError('Вы загрузили не изображение')

        img = Image.open(image)

        min_height, min_width = MIN_RESOLUTION_IMAGE
        if img.height < min_height or img.width < min_width:
            raise forms.ValidationError('Разрешение изображения меньше минимального')

        max_height, max_width = MAX_RESOLUTION_IMAGE
        if img.height > max_height or img.width > max_width:
            raise forms.ValidationError('Разрешение изображения больше максимального')

        if image.size > MAX_SIZE_BYTES_IMAGE:
            raise forms.ValidationError('Размер загруженного изображения больше 5 Мб')

        return cleaned_data
