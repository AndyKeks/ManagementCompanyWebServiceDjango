import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from .constants import HELP_TEXT_NUMBER_PHONE, PATTERN_NUMBER_PHONE
from .models import OrganisationProfile


class ExtendedAccountCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

        labels = {
            'username': _('Придумайте логин'),
            'email': _('Электронная почта'),
            'first_name': _('Имя'),
            'last_name': _('Фамилия'),
        }

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class OrganisationProfileForm(ModelForm):
    class Meta:
        model = OrganisationProfile
        fields = ('name', 'address', 'phone_number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].help_text = HELP_TEXT_NUMBER_PHONE

    def clean(self):
        cleaned_data = super(OrganisationProfileForm, self).clean()
        phone_number = cleaned_data.get('phone_number')

        if re.match(PATTERN_NUMBER_PHONE, phone_number) is None:
            raise forms.ValidationError(f'{phone_number} не соответствует примеру телефона')

        return self.cleaned_data
