from django.urls import path

from app_cadastro import views

urlpatterns = [
    #rota, #view resp, #nome da referência
    #cadastro.com
    path('',views.home,name = 'home'),
    #usuarios.com/usuarios
    path('usuarios/',views.usuarios,name='listagem_usuarios')
]
