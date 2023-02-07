from django.urls import path
from .views import allEmployes, detailEmployes, EmpleadoCreateView, SuccessView, EmpleadoUpdateView, EmpleadoDeleteView

app_name = 'empleados_app'

urlpatterns = [
    path('', allEmployes.as_view(), name="list_employes"),
    path('add-employe/', EmpleadoCreateView.as_view(), name="addEmploye"),
    path('edit-employe/<pk>/', EmpleadoUpdateView.as_view(), name="edit"),
    path('detail-employe/<pk>/', detailEmployes.as_view(), name="detail"),
    path('delete-employe/<int:id>/', EmpleadoDeleteView, name="delete")
]
