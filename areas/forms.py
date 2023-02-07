from django import forms
from .models import Area

class AreaForm(forms.ModelForm):
    
    class Meta:
        model = Area
        fields = ("nombreArea", "descripcionArea")
        labels = {
            'nombre': 'Nombre del Area',
            'descripcionArea': 'Descripcion del Area'
        }
        widgets = {
            'nombreArea' : forms.TextInput( attrs={ 'class': 'form-control' } ),
            'descripcionArea' : forms.TextInput( attrs={ 'class': 'form-control' } )
        }