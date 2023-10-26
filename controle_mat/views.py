from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CreateUserForm
from .models import Aluno

# Create your views here.
def index(request):
    alunos = Aluno.objects.all()
    return render(request, 'index.html', {'alunos': alunos})


def createStudent(request):
    if request.method == "POST":
        form = createStudent(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/")
    else:
        form = createStudent()

    return render(request, "createStudent.html", {"form": form})