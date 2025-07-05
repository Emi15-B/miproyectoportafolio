from django.urls import path, include
from rest_framework import routers
from .views import ProyectoViewSet, home, detalle_proyecto, sobre_mi, contacto
from . import views

router = routers.DefaultRouter()
router.register(r'api/proyectos', ProyectoViewSet)  

urlpatterns = [
    path('', home, name='home'),  
    path('proyecto/<int:proyecto_id>/', detalle_proyecto, name='detalle_proyecto'),  
    path('api/', include(router.urls)), 
    path('sobre-mi/', sobre_mi, name='sobre_mi'),
    path('contacto/', contacto, name='contacto'),
    path('productos/', views.productos_personalizados, name='productos_personalizados'),
]



