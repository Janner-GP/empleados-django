from django.urls import path
from . import views

app_name = 'cargos_app'

urlpatterns = [
    path('', views.cargoListView, name='list-cargos'),
    path('new-cargos/', views.cargoCreateView, name='addcargo'),
    path('edit-cargo/<int:id>/', views.cargoUpdateView, name='updatecargo'),
    path('delete-cargo/<int:id>/', views.cargoDeleteView, name='deletecargo'),
]