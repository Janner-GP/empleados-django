from django.urls import path
from . import views

app_name = 'areas_app'

urlpatterns = [
    path('', views.areaListView, name='list-areas'),
    path('new-area/', views.areaCreateView, name='addarea'),
    path('edit-area/<int:id>/', views.areaUpdateView, name='updatearea'),
    path('delete-area/<int:id>/', views.areaDeleteView, name='deletearea'),
]
