from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    
    class Meta:
        model = Empleado
        fields = ["nombreEmpleado", "apellidoEmpleado", "cargo", "avatar"]
        labels = {
            'nombreEmpleado': 'Nombre del Empleado',
            'apellidoEmpleado': 'Apellido del Empleado',
            'cargo': 'Cargo del Empleado'
        }
        widgets = {
            'nombreEmpleado':forms.TextInput( attrs={ 'class':'form-control' } ),
            'apellidoEmpleado':forms.TextInput( attrs={ 'class':'form-control' } ),
            'cargo': forms.Select( attrs= {'class': 'form-select'}),
            'avatar': forms.FileInput( attrs= {'class': 'form-control'})
        }
    
