from rest_framework import viewsets
from .models import Proyecto, MensajeContacto, ProductosPersonalizados
from .serializers import ProyectoSerializer

from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm
from django.contrib import messages

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

def home(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'portafolio/home.html', {'proyectos': proyectos})

def detalle_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    return render(request, 'portafolio/detalle.html', {'proyecto': proyecto})

def sobre_mi(request):
    return render(request, 'portafolio/sobre_mi.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            MensajeContacto.objects.create(
                nombre=form.cleaned_data['nombre'],
                email=form.cleaned_data['email'],
                mensaje=form.cleaned_data['mensaje']
            )
            send_mail(
                subject=f"Nuevo mensaje de {form.cleaned_data['nombre']}",
                message=f"Correo: {form.cleaned_data['email']}\n\nMensaje:\n{form.cleaned_data['mensaje']}",
                from_email=None,
                recipient_list=['maryelisberrios42@gmail.com'],
            )
            messages.success(request, 'Tu mensaje ha sido enviado con éxito.')
            return redirect('contacto')
    else:
        form = ContactForm()

    mi_contacto = {
        'correo': 'maryelisberrios42@gmail.com',
        'telefono': '+58 412-7260287',
        'instagram': '@emileth_b15',
        'instagram_emprendimiento': '@impresiones_byb1',
        'ubicacion': 'Barinas, Venezuela'
    }

    return render(request, 'portafolio/contacto.html', {
        'form': form,
        'mi_contacto': mi_contacto
    })

def productos_personalizados(request):
    productos = ProductosPersonalizados.objects.all()
    return render(request, 'portafolio/productos.html', {'productos': productos})