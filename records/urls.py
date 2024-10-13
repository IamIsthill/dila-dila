from django.urls import path
from records import views
    
urlpatterns = [
    path('', views.check_up_home, name='check_up_home'),
    path('record/add/', views.post_create_checkup, name='create_checkup'),
    path('record/update/<int:pk>', views.post_update_checkup, name='update_checkup'),
    path('record/delete/<int:pk>', views.post_delete_checkup, name='delete_checkup'),
    
]
