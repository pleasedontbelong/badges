from django.contrib import admin
from .models import Model3D


@admin.register(Model3D)
class Model3dAdmin(admin.ModelAdmin):
    pass
