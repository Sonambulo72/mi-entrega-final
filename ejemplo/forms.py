from django import forms
from django.contrib import admin # login y pass
from ejemplo.models import Familiar

admin.site.register(Familiar) #login y pass


class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']