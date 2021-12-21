from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        invalidInputs = ["", None]

        if User.objects.count() == 0:
            for user in settings.ADMINS:
                username = user[0].replace(' ', '')
                email = user[1]
                password = user[2]
                if username.strip() in invalidInputs or password.strip() in invalidInputs:
                    return None

                user = User(
                    username=username,
                    email=email,
                )
                user.set_password(password)
                user.is_superuser = True
                user.is_staff = True
                user.save()


        else:
            print('Admin accounts can only be initialized if no Accounts exist')
