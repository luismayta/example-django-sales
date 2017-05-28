from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')


class UserChangeForm(UserChangeForm):
    def __init__(self, *args, **kargs):
        super(UserChangeForm, self).__init__(*args, **kargs)
        del self.fields['is_staff']

    class Meta:
        # solo defines el model por que las demas propiedades las hereda del UserChangeForm.Meta
        model = User
        exclude = ['', ]
