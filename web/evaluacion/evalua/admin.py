from django.contrib import admin

from .models import*

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'lastname', 'email')
    search_fields = ['user', 'name']

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'correo', 'telefono', 'fk_usuario')
    search_fields = ['nombre', 'direccion']

class BusAdmin(admin.ModelAdmin):
    list_display = ('capacidad', 'estado', 'num_bus', 'climatizado', 'fk_empresa')
    search_fields = ['capacidad']

class RutaAdmin(admin.ModelAdmin):
    list_display = ('region', 'descripcion')
    search_fields = [ 'region']

class ViajeAdmin(admin.ModelAdmin):
    list_display = ('origen', 'destino', 'fecha_hora', 'precio', 'clase', 'cupo', 'fk_ruta', 'fk_bus')
    search_fields = [ 'destino']

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'telefono', 'direccion', 'cedula', 'foto_perfil')
    search_fields = ['usuario', 'cedula']

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Bus, BusAdmin)
admin.site.register(Ruta, RutaAdmin)
admin.site.register(Viaje, ViajeAdmin)
admin.site.register(Perfil, PerfilAdmin)

