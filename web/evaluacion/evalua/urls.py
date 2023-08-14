from rest_framework import routers
from .viewset import *

ruta = routers.SimpleRouter()
ruta.register('api/v1.0/empresa', EmpresaViewset)
ruta.register('api/v1.0/viaje', ViajeViewset)
ruta.register('api/v1.0/usuario', UsuarioViewset)
ruta.register('api/v1.0/ruta', RutaViewset)
ruta.register('api/v1.0/bus', BusViewset)

urlpatterns = ruta.urls