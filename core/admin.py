from django.contrib import admin
from .models import Aluno, Aula, Momento

# Register your models here.
admin.site.register(Aluno)
admin.site.register(Aula)
admin.site.register(Momento)