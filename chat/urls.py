
from django.urls import path
from .views import room, base_view

urlpatterns = [
    
    path('<str:room_name>/<str:username>/', room, name='room'),
    path('', base_view, name='base_view'),

]
