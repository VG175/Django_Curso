from django.urls import path
from .import views

urlpatterns = [        
    path('',views.listaTarefa, name = 'lista_tarefa'),
    path('novaTarefa/', views.novaTarefa, name='nova_tarefa'),
]
