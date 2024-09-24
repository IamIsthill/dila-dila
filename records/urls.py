from django.urls import path
from records import views
    
urlpatterns = [
    path('', views.check_up_home, name='check_up_home'),
    path('record/<int:pk>', views.post_update_checkup, name='update_checkup'),
    
]
