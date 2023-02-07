from django.shortcuts import render
from .models import Cargo
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CargoForm
from django.contrib import messages

# Create your views here.
def cargoListView(request):
    template = 'cargos/allCargos.html'
    cargos = Cargo.objects.all()
    context = {'cargos': cargos}
    return render(request, template, context)

def cargoCreateView(request):
    template = 'cargos/newCargo.html'
    if request.method == 'POST':
        form_cargo = CargoForm(request.POST, request.FILES)
        if form_cargo.is_valid():
            form_cargo.save()
            messages.success(request, "Cargo creado con exito")
            return redirect(to="cargos_app:list-cargos")
    else:
        form_cargo = CargoForm()

    context = { "form":form_cargo }
    return render(request, template, context)

def cargoUpdateView(request, id):
    template = 'cargos/updateCargo.html'
    cargo = get_object_or_404(Cargo, id=id)
    form_cargo = CargoForm(
        request.POST or None,
        instance=cargo
    )

    if form_cargo.is_valid():
        form_cargo.save()
        messages.success(request, "Cargo actualizado con éxito")
        return redirect(to="cargos_app:list-cargos")

    context = { 'form':form_cargo, 'cargo':cargo }
    return render(request, template, context)


def cargoDeleteView(request, id):
    cargo = get_object_or_404(Cargo, id=id)
    cargo.delete()
    messages.success(request, "Cargo eliminado con éxito")
    return redirect(to="cargos_app:list-cargos")