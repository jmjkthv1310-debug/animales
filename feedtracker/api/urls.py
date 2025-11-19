from django.urls import path
from . import views

urlpatterns = [
    path('preguntas/', views.listar_preguntas),
    path('preguntas/crear/', views.crear_pregunta),
    path('preguntas/<int:id>/', views.obtener_pregunta),
    path('preguntas/<int:id>/actualizar/', views.actualizar_pregunta),
    path('preguntas/<int:id>/eliminar/', views.eliminar_pregunta),
]
