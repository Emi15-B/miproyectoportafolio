from django.urls import include, path
from rest_framework import routers
from .views import ProyectoViewSet

router = routers.DefaultRouter()
router.register(r'proyectos', ProyectoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
