from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('task',views.task,name='task'),
    path('data',views.data,name='data'),

    
]