from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from core.models import Aluno, Aula
from .forms import AlunoForm
import subprocess


# Create your views here.
def list_all(request):
    alunos = Aluno.objects.all()
    aula = Aula.objects.get(pk=1)
    return render(request, 'list_all.html', {'alunos': alunos, 'aula': aula})


def add_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = AlunoForm()

    return render(request, 'add.html', {'form': form})

def start_aula(request):
    aula = Aula.objects.get(pk=1)
    aula.active = True
    aula.save()
    p = subprocess.Popen("python manage.py recognize", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return redirect('/')

def end_aula(request):
    aula = Aula.objects.get(pk=1)
    aula.active = False
    aula.save()
    return redirect('/')

def get_alunos(request):
    alunos = Aluno.objects.all()
    json = serializers.serialize('json', alunos)
    return HttpResponse(json, content_type='application/json')
