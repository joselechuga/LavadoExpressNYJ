from django.urls import path
from .views import index,carpinteria   

urlpatterns = [
    path('',index,name='index'),
    path('carpinteria/',carpinteria,name='carpinteria'),

]