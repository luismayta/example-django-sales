# Register your models here.
from django.contrib import admin
from .forms import RegisterUserForm
from .models import RegisterUser


@admin.register(RegisterUser)
class RegisterUserAdmin(admin.ModelAdmin):
    form = RegisterUserForm
    list_display = ('email', 'username', 'date_joined')
