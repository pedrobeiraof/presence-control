# Generated by Django 2.0.6 on 2018-10-03 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181003_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='alunos',
            field=models.ManyToManyField(related_name='aulas', to='core.Aluno'),
        ),
    ]
