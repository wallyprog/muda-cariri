from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Perfil)
admin.site.register(Anuncio)
admin.site.register(Transacao)