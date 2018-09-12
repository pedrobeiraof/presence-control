from django.forms import ModelForm
from core.models import Aluno

# Create the form class.
class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'foto']