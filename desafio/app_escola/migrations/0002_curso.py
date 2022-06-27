# Generated by Django 4.0.5 on 2022-06-27 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_escola', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_curso', models.CharField(max_length=100)),
                ('ativo', models.BooleanField(default=True)),
                ('inicio', models.DateField()),
                ('termino', models.DateField()),
                ('professor', models.OneToOneField(limit_choices_to={'groups__name': 'Professores'}, on_delete=django.db.models.deletion.CASCADE, related_name='Professor', to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(limit_choices_to=({'groups__name': 'Alunos'}, None), null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
