
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from portafolio.views import ProyectoViewSet

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'proyectos', ProyectoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('portafolio.urls')),  
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)