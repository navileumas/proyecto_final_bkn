from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from django.core.mail import send_mail

def buscar_libros(request):
    query = request.GET.get('q', '')
    libros = Libro.objects.filter(titulo__icontains=query) if query else []
    return render(request, 'libros/templates/buscar.html', {'libros': libros, 'query': query})

def mostrar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/templates/lista.html', {'libros': libros})

def insertar_libro(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        fecha_publicacion = request.POST['fecha_publicacion']
        isbn = request.POST['isbn']

        libro = Libro.objects.create(
            titulo=titulo,
            autor=autor,
            fecha_publicacion=fecha_publicacion,
            isbn=isbn
        )
        
        # Enviar un correo usando Mailtrap
        send_mail(
            'Nuevo libro agregado',
            f'Se ha registrado el libro "{libro.titulo}" de {libro.autor}.',
            'noreply@biblioteca.com',
            ['samuel.quirozangel@cesunbc.edu.mx'],  
        )

        return redirect('mostrar_libros')
    
    return render(request, 'libros/templates/formulario.html')
