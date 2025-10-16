from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado
from datetime import date # Necesario para manejar el campo DateField

# Listar empleados
def index(request):
    empleados = Empleado.objects.all()
    return render(request, 'listar_empleados.html', {'empleados': empleados})

# Ver empleado (opcional, puedes usarlo si quieres detalle)
def ver_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    # Si quieres una página de detalle para ver_empleado, necesitarías
    # crear un template llamado 'ver_empleado.html' en app_empleados/templates/
    # Por ahora, solo es un marcador de posición si no lo vas a usar.
    return render(request, 'ver_empleado.html', {'empleado': empleado}) 

# Agregar empleado
def agregar_empleado(request):
    if request.method == 'POST':
        id_empleado = request.POST['id_empleado']
        id_sucursal = request.POST['id_sucursal']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        cargo = request.POST['cargo']
        
        # Convertir la cadena de fecha a un objeto date
        fecha_contratacion_str = request.POST['fecha_contratacion']
        fecha_contratacion = date.fromisoformat(fecha_contratacion_str)

        Empleado.objects.create(
            id_empleado=id_empleado,
            id_sucursal=id_sucursal,
            nombre=nombre,
            apellido=apellido,
            cargo=cargo,
            fecha_contratacion=fecha_contratacion
        )
        return redirect('inicio')
    return render(request, 'agregar_empleado.html')

# Editar empleado
def editar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.id_empleado = request.POST['id_empleado']
        empleado.id_sucursal = request.POST['id_sucursal']
        empleado.nombre = request.POST['nombre']
        empleado.apellido = request.POST['apellido']
        empleado.cargo = request.POST['cargo']
        
        # Convertir la cadena de fecha a un objeto date
        fecha_contratacion_str = request.POST['fecha_contratacion']
        empleado.fecha_contratacion = date.fromisoformat(fecha_contratacion_str)
        
        empleado.save()
        return redirect('inicio')
    return render(request, 'editar_empleado.html', {'empleado': empleado})

# Borrar empleado
def borrar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('inicio')
    return render(request, 'borrar_empleado.html', {'empleado': empleado})