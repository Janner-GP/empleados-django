from django.contrib import admin
from .models import Empleado
from cargos.models import Cargo

# Register your models here.
class EmpleadoAdmin(admin.ModelAdmin):

    def area(self, obj):
        return obj.cargo.Area.nombreArea

    list_display = (
        'id',
        'nombreEmpleado',
        'apellidoEmpleado',
        'cargo',
        'area'
    )

    search_fields = ('nombreEmpleado', 'apellidoEmpleado')
    list_filter = ('cargo',)

admin.site.register(Empleado, EmpleadoAdmin)