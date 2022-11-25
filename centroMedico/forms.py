from django import forms
from django.forms import ModelForm
from .models import Paciente

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre','apellido','email','contraseña']