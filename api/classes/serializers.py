from rest_framework.serializers import ModelSerializer
from .models import Aluno

class AlunosSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'