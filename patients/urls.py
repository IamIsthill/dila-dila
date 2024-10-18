from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_list, name="patient-list"),
    path('<int:pk>/', views.patient, name="patient"),
    path('add/', views.add_patient_view, name="add-patient"),
    path('edit/<int:pk>/', views.edit_patient_view, name="edit-patient"),
    # path('delete/<int:pk>/', views.delete_patient_view, name="delete-patient")
]
