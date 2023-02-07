from django.shortcuts import render
from .models import Empleado
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from .forms import EmpleadoForm

# Create your views here.
class allEmployes(ListView):
    context_object_name = 'listEmployes'
    template_name = 'empleados/allEmployes.html'
    paginate_by = 4
    ordering = 'nombreEmpleado'

    def get_queryset(self):
        lista = Empleado.objects.all()
        nameSearch = self.request.GET.get('nameSearch', '')
        lista = Empleado.objects.filter(
            fullnameEmpleado__icontains = nameSearch
        )
        return lista

class detailEmployes(DetailView):
    model = Empleado
    template_name = 'empleados/detailEmployes.html'

class SuccessView(TemplateView):
    template_name = "empleados/success.html"

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "empleados/addEmployes.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados_app:list_employes')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            empleado = form.save(commit=False)
            empleado.fullnameEmpleado = empleado.nombreEmpleado + ' ' + empleado.apellidoEmpleado
            empleado.save()
            messages.success(request, "Guardado con Exito")
            return self.form_valid(form)
        else:
            messages.error(request, "Algo salio mal")
            return self.form_invalid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "empleados/editEmploye.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados_app:list_employes')

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.fullnameEmpleado = empleado.nombreEmpleado + ' ' + empleado.apellidoEmpleado
        empleado.save()
        return super(EmpleadoUpdateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(request, "Guardado con Exito")
        return super().post(request, *args, **kwargs)


def EmpleadoDeleteView(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    empleado.delete()
    messages.success(request, "Registro Eliminado con Exito")
    return redirect(to='empleados_app:list_employes')


    