from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Curso
from django.urls import reverse


# Create your views here.
def home(request):
    return render(request, "app_escola/home.html")


def redirect(request):

    if request.user.groups.filter(name='Professores').exists():
        return HttpResponseRedirect("prof_home")

    elif request.user.groups.filter(name='Alunos').exists():
        return HttpResponseRedirect("aluno_home")

    elif request.user.is_staff:
        return HttpResponseRedirect("/admin")

    else:
        return HttpResponseRedirect("error_page")

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Professores').exists())
def prof_home(request):
    return render(request, "app_escola/prof_home.html")

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Alunos').exists())
def aluno_home(request):
    return render(request, "app_escola/aluno_home.html")

def error_page(request):
    return render(request, "app_escola/error_page.html")