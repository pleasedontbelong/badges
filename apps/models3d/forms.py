from django import forms
from .models import Model3D


class Model3dCreateForm(forms.ModelForm):
    class Meta:
        model = Model3D
        fields = ['name']

    def __init__(self, *args, **kwargs):
        self.profile = kwargs.pop('profile')
        super(Model3dCreateForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.profile = self.profile
        super(Model3dCreateForm, self).save(*args, **kwargs)
