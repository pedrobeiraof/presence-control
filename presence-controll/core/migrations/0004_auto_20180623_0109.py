# Generated by Django 2.0.6 on 2018-06-23 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_aluno_is_presente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='is_presente',
            field=models.BooleanField(default=False),
        ),
    ]