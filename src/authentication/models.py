from django.conf import settings
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string


class RegisterUser(models.Model):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        verbose_name='nombre de usuario',
        max_length=150,
        unique=True,
        validators=[username_validator]
    )
    email = models.EmailField(
        verbose_name='email',
        unique=True
    )
    password = models.CharField(
        verbose_name='password',
        max_length=128
    )
    token = models.CharField(
        verbose_name='token',
        max_length=32
    )
    date_joined = models.DateTimeField(
        verbose_name='date joined',
        default=timezone.now
    )

    class Meta:
        verbose_name = 'registro usuario temporal'
        verbose_name_plural = 'registro usuarios temporales'

    def __str__(self):
        return self.email

    def save(self, **kwargs):
        if not self.id:
            self.token = self._generate_token()
        return super().save(**kwargs)

    def _generate_token(self):
        while True:
            token = get_random_string(length=32)
            if not RegisterUser.objects.filter(token=token):
                return token

    @staticmethod
    def delete_expired_registers():
        """Elimina usuarios expirados."""
        days = settings.AUTH_REGISTER_EXPIRE_DAYS
        diff = timezone.now() - timezone.timedelta(days=days)
        RegisterUser.objects.filter(date_joined__lt=diff).delete()
