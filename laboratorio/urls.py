from django.urls import path
#from . import views
#from .views import IndexPageView, indexV, agregarV, modificarV, listarV
from .views import registro_view, login_view, logout_view, \
    eliminarlaboratorio_view, agregar_laboratorio_view, \
    editar_laboratorio_view, \
    Bienvenido, Primero

urlpatterns = [
    path('primero/editar-laboratorio/<int:id>/', editar_laboratorio_view, name='editar_laboratorio'),
    path('agregar-laboratorio/', agregar_laboratorio_view, name='agregar_laboratorio'),
    path('primero/eliminarlaboratorio/<id>', eliminarlaboratorio_view, name='eliminarlaboratorio'),
    path('registro/', registro_view, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', Bienvenido, name ='bienvenido'),
    path('primero/', Primero, name ='primero'),
]