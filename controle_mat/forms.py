from django import forms
from .models import Aluno

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'endereco', 'email', 'data_de_nascimento', 'cidade', 'curso']

