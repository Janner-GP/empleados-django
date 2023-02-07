from django.shortcuts import render
from .models import Area
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AreaForm
from django.contrib import messages

# Create your views here.
def areaListView(request):
    template = 'areas/listAreas.html'
    areas = Area.objects.all
    context = {'areas':areas}
    return render(request, template, context)

def areaCreateView(request):
    template = 'areas/newArea.html'
    if request.method == 'POST':
        form_area = AreaForm(request.POST, request.FILES)
        if form_area.is_valid():
            form_area.save()
            messages.success(request, "Area creada con exito")
            return redirect(to='areas_app:list-areas')
    else:
        form_area = AreaForm()

    context ={'form':form_area}
    return render(request, template, context)

def areaUpdateView(request, id):
    template = 'areas/updateArea.html'
    area = get_object_or_404(Area, id=id)
    form_area = AreaForm(
        request.POST or None,
        instance=area
    )

    if form_area.is_valid():
        form_area.save()
        messages.success(request, "Area actualizado con éxito")
        return redirect(to="areas_app:list-areas")

    context = { 'form':form_area, 'area':area }
    return render(request, template, context)

def areaDeleteView(request, id):
    area = get_object_or_404(Area, id=id)
    area.delete()
    messages.success(request, "Area eliminada con éxito")
    return redirect(to="areas_app:list-areas")
