from django.urls import path
from . import views

urlpatterns = [
    path('', views.request_list_view, name="request-list"),
    path('add/', views.add_request_view, name="add-request"),
    path('<int:pk>/', views.request_view, name="request"),
    path('toggle/<int:pk>/', views.request_toggle, name="request-toggler"),
    path('update/<int:pk>/', views.update_request_view, name="update-request"),
    path('delete/<int:pk>/', views.delete_request_view, name="delete-request"),
]
