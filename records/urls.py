from django.urls import path
from records import views
    
urlpatterns = [
    path('', views.check_up_home, name='check_up_home')
    
]
