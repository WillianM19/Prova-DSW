from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import CreateUserForm
from .models import Aluno

# Create your views here.
def index(request):
    alunos = Aluno.objects.all()
    return render(request, 'index.html', {'alunos': alunos})

def createStudent(request):
   if request.method == "POST":
       form = CreateUserForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponseRedirect('/')
       else:
           return render(request, 'createStudent.html', {'form': form})
   else:
       form = CreateUserForm()
       return render(request, 'createStudent.html', {'form': form})
   
def deleteStudent(request, id):
  aluno = Aluno.objects.get(id=id)
  aluno.delete()
  return HttpResponseRedirect('/')

def showStudent(request, id):
    aluno = Aluno.objects.get(id=id)
    return render(request, 'showStudent.html', {'aluno': aluno})


def editStudent(request, id):
   aluno = Aluno.objects.get(id=id)
   if request.method == "POST":
       form = CreateUserForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponseRedirect('/')
       else:
           return render(request, 'createStudent.html', {'form': form})
   else:
       form = CreateUserForm()
       return render(request, 'createStudent.html', {'form': form})