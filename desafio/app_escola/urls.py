from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('redirect', views.redirect),
    path('prof_home', views.prof_home),
    path('aluno_home', views.aluno_home),
    path('error_page', views.error_page),
]
