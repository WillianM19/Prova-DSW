from django.shortcuts import render
from .models import Aluno

# Create your views here.
def index(request):
    alunos = Aluno.objects.all()
    return render(request, 'index.html', {'alunos': alunos})