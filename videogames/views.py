from django.shortcuts import render, redirect, get_object_or_404
from .models import Videogame


def videogame_list(request):
    videogames = Videogame.objects.all()
    return render(request, 'videogames/list.html', {'videogames': videogames})


def videogame_detail(request, pk):
    videogame = get_object_or_404(Videogame, pk=pk)
    return render(request, 'videogames/detail.html', {'videogame': videogame})


def videogame_create(request):
    if request.method == 'POST':
        # Validación server-side: evita que usuarios malintencionados envíen
        # datos vacíos desactivando JavaScript o manipulando el HTML del navegador
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        launch_date = request.POST.get('launch_date', '').strip()

        # Si algún campo está vacío, retorna el formulario con mensaje de error
        if not title or not description or not launch_date:
            return render(request, 'videogames/form.html', {
                'error': 'Todos los campos son obligatorios',
                'form_data': request.POST
            })

        Videogame.objects.create(
            title=title,
            description=description,
            launch_date=launch_date
        )
        return redirect('videogame_list')
    return render(request, 'videogames/form.html')


def videogame_update(request, pk):
    videogame = get_object_or_404(Videogame, pk=pk)
    if request.method == 'POST':
        # Validación server-side: protege la integridad de los datos
        # incluso si el cliente omite la validación HTML5
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        launch_date = request.POST.get('launch_date', '').strip()

        if not title or not description or not launch_date:
            return render(request, 'videogames/form.html', {
                'videogame': videogame,
                'error': 'Todos los campos son obligatorios',
                'form_data': request.POST
            })

        videogame.title = title
        videogame.description = description
        videogame.launch_date = launch_date
        videogame.save()
        return redirect('videogame_list')
    return render(request, 'videogames/form.html', {'videogame': videogame})


def videogame_delete(request, pk):
    videogame = get_object_or_404(Videogame, pk=pk)
    # DELETE usa POST en Django tradicional porque los formularios HTML
    # solo soportan GET y POST de forma nativa
    if request.method == 'POST':
        videogame.delete()
        return redirect('videogame_list')
    return render(request, 'videogames/confirm_delete.html', {'videogame': videogame})
