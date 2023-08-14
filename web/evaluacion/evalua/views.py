from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import*
from django.urls import reverse_lazy


from .forms import *
from .models import *

def login_view(request):
   if request.user.is_authenticated:
        return HttpResponseRedirect('/lista_empresa/')
   else:
       if request.method == 'POST':
           form = LoginForm(request.POST)
           if form.is_valid():
               username = form.cleaned_data['username']
               password = form.cleaned_data['password']
               usuario = authenticate(username = username, password= password)
               if usuario is not None and usuario.is_active: 
                   login(request,usuario)
                   return HttpResponseRedirect('/lista_empresa/')
        
       form = LoginForm()
       ctx = {'form' : form}
       return render(request, 'login.html', ctx)
   
@login_required(login_url='/login/')
def inicio_view(request):
    empresas = Empresa.objects.all()
    ctx = {'empresas': empresas}
    return render(request, 'index.html', ctx)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def registrar_view(request):
    info = "Inicializar"
    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            perfil = Perfil()
            perfil.usuario = user
            perfil.telefono = form.cleaned_data['telefono']
            perfil.direccion = form.cleaned_data['direccion']
            perfil.cedula = form.cleaned_data['cedula']
            perfil.foto = form.cleaned_data['foto']
            perfil.save()
            info = "Guardado Satisfactoriamente!!"
            ctx = {'info': info}
            return render(request, 'registro_exitoso.html', ctx)
    
    else:
        form = PerfilForm()
        form.fields['username'].help_text = None
        form.fields['password1'].help_text = None
        form.fields['password2'].help_text = None

    ctx = {'form': form}
    return render(request, 'registro_usuario.html', ctx)

class ListaEmpresa(ListView):
    model = Empresa
    template_name= 'dashboard/listar_producto.html'
    queryset = Empresa.objects.all()
    context_object_name = 'empresas_lista'

class CrearEmpresa(CreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'dashboard/crear_producto.html'
    success_url = reverse_lazy('listar_empresa')

class ActualizarEmpresa(UpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'dashboard/editar_producto.html'
    success_url = reverse_lazy('listar_empresa')

class EliminarEmpresa(DeleteView):
    model = Empresa
    template_name = 'dashboard/producto_delete.html'
    def post(self, request, pk, *args, **kwargs):
        object = Empresa.objects.get(id=pk)
        object.delete()     
        return redirect('listar_empresa')
    

class ListaUsuario(ListView):
    model = Usuario
    template_name= 'dashboard/listar_proveedor.html'
    queryset = Usuario.objects.all()
    context_object_name = 'usuarios_lista'
 
class CrearUsuario(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'dashboard/crear_proveedor.html'
    success_url = reverse_lazy('listar_usuario')
     
class ActualizarUsuario(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'dashboard/editar_proveedor.html'
    success_url = reverse_lazy('listar_usuario')
    
class EliminarUsuario(DeleteView):
    model = Usuario
    template_name = 'dashboard/proveedor_delete.html'
    def post(self, request, pk, *args, **kwargs):
        object = Usuario.objects.get(id=pk)
        object.delete()     
        return redirect('listar_usuario')
    

class ListaViaje(ListView):
    model = Viaje
    template_name= 'dashboard/listar_viaje.html'
    queryset = Viaje.objects.all()
    context_object_name = 'viajes_lista'
 
class CrearViaje(CreateView):
    model = Viaje
    form_class = ViajeForm
    template_name = 'dashboard/crear_viaje.html'
    success_url = reverse_lazy('listar_viaje')
     
class ActualizarViaje(UpdateView):
    model = Viaje
    form_class = ViajeForm
    template_name = 'dashboard/editar_viaje.html'
    success_url = reverse_lazy('listar_viaje')
    
class EliminarViaje(DeleteView):
    model = Viaje
    template_name = 'dashboard/viaje_delete.html'
    def post(self, request, pk, *args, **kwargs):
        object = Viaje.objects.get(id=pk)
        object.delete()     
        return redirect('listar_viaje')
    

