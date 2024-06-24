from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', include('users.urls')),
    path('patients/', include('patients.urls')),
    path('medicine-requests/', include('medicine_request.urls')),
    path('api/get-all-patients', views.all_patient_count, name="get-all-patients"),
    path('api/get-monthly-patients', views.monthly_patient_count, name="get-monthly-patients"),
    path('api/get-today-patients', views.today_patient_count, name="get-today-patients"),
    path('api/get-all-requests', views.all_request_count, name="get-all-requests"),
    path('api/get-monthly-requests', views.monthly_request_count, name="get-monthly-requests"),
    path('api/get-today-requests', views.today_request_count, name="get-today-requests"),
    path('api/get-all-medicine', views.all_medicine_count, name="get-all-medicine"),
    path('api/get-monthly-medicine', views.monthly_medicine_count, name="get-monthly-medicine"),
    path('api/get-today-medicine', views.today_medicine_count, name="get-today-medicine"),
    path('reports/', views.generate_report, name="report")
]
