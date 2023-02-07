from django import forms
from .models import Cargo

class CargoForm(forms.ModelForm):
    
    class Meta:
        model = Cargo
        fields = ("nombreCargo", "descripcionCargo", "Area")
        labels = {
            "nombreCargo": "Nombre del Cargo",
            "descripcionCargo": "Descripcion del Cargo",
            "Area": "Area del Cargo"
        }
        widgets = {
            'nombreCargo': forms.TextInput( attrs= { 'class': 'form-control' }),
            'descripcionCargo': forms.TextInput( attrs= { 'class': 'form-control' }),
            'Area': forms.Select( attrs= {'class': 'form-select'})
        }